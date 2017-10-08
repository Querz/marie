<template>
  <div class="profile">
    <img v-if="showWelcome" src="../assets/welcome.gif" class="welcome" v-on:click="showWelcome = false"/>
    <template v-else>
      <h1>Questionaire</h1>
      <ui-progress-linear
        color="white"
        type="determinate"
        :progress="progress"
      ></ui-progress-linear>
      <div class="marie">
        <img v-if="basicInfo" src="../assets/marie1.svg"/>
        <img v-if="moreInfo" src="../assets/marie2.svg"/>
      </div>
      <div class="questions">
        <template v-if="basicInfo">
          <ui-autocomplete
            error="This field is required"
            :invalid="cityTouched && !profile.new_residence.length > 0"
            @touch="cityTouched = true"
            label="Where are you moving to?"
            placeholder="Enter the name of the city"
            :suggestions="cities"
            v-model="profile.new_residence"
          ></ui-autocomplete>
          <ui-select
            has-search
            label="What is your Nationality?"
            :keys="{ label: 'name', value: 'code' }"
            :options="sortedCountries"
            v-model="profile.nationality"
          ></ui-select>
          <ui-datepicker
            label="When are you moving?"
            :min-date="today"
            v-model="profile.move_date"
          ></ui-datepicker>
        </template>
        <template v-if="moreInfo">
          <ui-select
            label="Tell us about yourself"
            multiple
            :keys="{ label: 'text', value: 'code' }"
            placeholder="Select everything that applies to you"
            :options="reasons"
            v-model="profile.move_reasons"
          ></ui-select>
          <label>What's your birthday?</label>
          <div class="birthdate">
            <ui-select
              class="day"
              placeholder="Day"
              :options="days"
              v-model="profile.birthdate.day"
            ></ui-select>
            <ui-select
              class="month"
              placeholder="Month"
              :options="months"
              :keys="{ label: 'text', value: 'code' }"
              v-model="profile.birthdate.month"
            ></ui-select>
            <ui-select
              class="year"
              placeholder="Year"
              :options="years"
              v-model="profile.birthdate.year"
            ></ui-select>
          </div>
        </template>
      </div>
      <div class="action">
        <a class="right" v-if="basicInfo && profile.new_residence.length > 0" v-on:click="toggleView()"><ui-icon>keyboard_arrow_right</ui-icon></a>
        <a class="left" v-if="moreInfo" v-on:click="toggleView()"><ui-icon>keyboard_arrow_left</ui-icon></a>
        <a class="right" v-if="moreInfo" v-on:click="sendProfile()"><ui-icon>keyboard_arrow_right</ui-icon></a>
      </div>
    </template>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueResource from 'vue-resource'
  import countries from '../data/countries'
  import cities from '../data/cities'
  import reasons from '../data/reasons'
  import months from '../data/months'
  import { UiSelect, UiDatePicker, UiAutoComplete, UiIcon, UiButton } from 'keen-ui'

  Vue.use(VueResource)
  const http = Vue.http

  export default {
    name: 'profile',
    components: {
      UiIcon,
      UiSelect,
      UiDatePicker,
      UiAutoComplete,
      UiButton
    },
    data () {
      return {
        basicInfo: true,
        moreInfo: false,
        profile: {
          // language: '0',
          // name: '',
          // age: 0,
          // religion: 0,
          nationality: {},
          new_residence: '',
          move_reasons: [],
          move_date: null,
          birthdate: {
            day: '',
            month: '',
            year: ''
          },
          age: 25
        },
        cityTouched: false,
        today: new Date(),
        countries,
        cities,
        reasons,
        months,
        progress: 33,
        showWelcome: true
      }
    },
    computed: {
      sortedCountries: function () {
        function compare (a, b) {
          if (a.name < b.name) {
            return -1
          }
          if (a.name > b.name) {
            return 1
          }
          return 0
        }
        return this.countries.sort(compare)
      },
      days: function () {
        let days = []
        for (var i = 1; i < 31; i++) {
          days.push(String(i))
        }
        return days
      },
      years: function () {
        let years = []
        for (var i = this.today.getFullYear(); i >= 1950; i--) {
          years.push(String(i))
        }
        return years
      }
    },
    methods: {
      toggleView () {
        this.basicInfo = !this.basicInfo
        this.moreInfo = !this.moreInfo
        this.progress = 66
      },
      sendProfile () {
        let prof = {}
        prof.move_reasons = []
        for (var i = 0; i < this.profile.move_reasons.length; i++) {
          prof.move_reasons.push(parseInt(this.profile.move_reasons[i].code))
        }
        prof.nationality = this.profile.nationality.code
        prof.new_residence = this.profile.new_residence
        prof.birthdate = this.profile.birthdate.year + '-' + this.profile.birthdate.month.code + '-' + this.profile.birthdate.day
        prof.move_date = this.profile.move_date
        http.post('http://localhost:9999/', JSON.stringify(prof), {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          // success
          window.location.href = '/#/main'
          console.log('response: ' + JSON.stringify(response.body))
        }, function (response) {
          // error callback
          console.log('err response: ' + JSON.stringify(response.body))
        })
      }
    }
  }
</script>

<style>
.profile h1, .profile h2 {
  font-weight: normal;
  padding: 0.5rem 0.75rem;
  color: #fff;
}
img.welcome {
  width: 100%;
  height: 667px;
}
.ui-progress-linear{
  margin-bottom: 1rem;
}
.marie {
  width: 100%;
  padding-top: 1rem;
  text-align: right;
}
.questions {
  padding-top: 2rem;
  padding-bottom: 1rem;
  padding-left: 2rem;
  padding-right: 2rem;
  width: 100%;
}
.ui-select__label-text {
  color: #fff;
}
.ui-datepicker__label-text {
  color: #fff;
}
.ui-autocomplete__label-text {
  color: #fff;
}
.action {
  padding: 0rem 1rem;
  cursor: pointer;
}
.action .ui-icon {
  font-size: 40px;
}
.profile {
  background: #fcd37f ;
  background: -moz-linear-gradient(-45deg, #fcd37f 0%, #ea9b6c 29%, #d55757 63%, #d55757 100%);
  background: -webkit-linear-gradient(-45deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  background: linear-gradient(135deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcd37f ', endColorstr='#d55757 ',GradientType=1 );
  height: 100vh;
}
.birthdate div.ui-select {
  float: left;
  width: 33%;
}
.action .right {
  float: right;
  text-align: right;
}
</style>
