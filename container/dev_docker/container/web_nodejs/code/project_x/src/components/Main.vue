<template>
  <div class="main">
    <div class="header padded">
      <img src="../assets/logo.svg"/>
      <h1 v-if="listview">Your List</h1>
      <h1 v-if="detailedview">Task Details</h1>
      <h1 v-if="mapview">Your Map</h1>
    </div>
    <template v-if="listview">
      <div class="list">
        <div v-for="todo in todolist" :key="todo.id" class="todo padded-todo" v-on:click="showDetails(todo.id)">
          <div class="title">
            <label v-if="todo.due !== null" class="right due">Due: {{ todo.due }}</label>
            <h2>{{ todo.title }}</h2>
          </div>
          <div class="content">
            <span v-if="!todo.date && !todo.time" class="right">
              <label class="mandatory" v-if="todo.mandatory"><ui-icon>fiber_manual_record</ui-icon> mandatory</label>
              <label class="optional" v-else><ui-icon>fiber_manual_record</ui-icon> optional</label>
            </span>
            <label v-if="todo.location !== null && todo.location !== ''">Place: {{ todo.location }}</label>
            <label v-else>Place: N/A</label>
            <span v-if="todo.date || todo.time" class="datetime">
              <span class="right">
                <label class="mandatory" v-if="todo.mandatory"><ui-icon>fiber_manual_record</ui-icon> mandatory</label>
                <label class="optional" v-else><ui-icon>fiber_manual_record</ui-icon> optional</label>
              </span>
              <label>{{ todo.date }}</label>
              <label>{{ todo.time }}</label>
            </span>
          </div>
        </div>
      </div>
    </template>
    <template v-if="detailedview">
      <template v-for="todo in todolist">
        <div v-if="todo.id === detailedStepID" :key="todo.id" class="details">
          <h2>{{ todo.title }}</h2>
          <div class="description">
            {{ todo.description }}
          </div>
          <div class="place-time">
            <label class="place" v-if="todo.location !== null && todo.location !== ''">Place: {{ todo.location }}</label>
            <div class="date-time" v-if="todo.date || todo.time">
              Date: <label>{{ todo.date }}</label> <label>{{ todo.time }}</label>
            </div>
            <label v-if="todo.due !== null" class="left due">Due: {{ todo.due }}</label>
            <span class="right">
              <label class="mandatory" v-if="todo.mandatory"><ui-icon>fiber_manual_record</ui-icon> mandatory</label>
              <label class="optional" v-else><ui-icon>fiber_manual_record</ui-icon> optional</label>
            </span>
          </div>
          <div class="status">
            <label v-if="todo.status === 1"><ui-icon>check</ui-icon> Done</label>
            <label v-if="todo.status === 0"><ui-icon>close</ui-icon> Pending</label>
          </div>
          <h2>Related Tasks</h2>
        </div>
      </template>
    </template>
    <template v-if="mapview">
      <div style="height=100%">
        <gmap-map
          id="map"
          :center="{lat: 48.473451, lng: 7.9498017}"
          :zoom="16" 
          class="map">
          <gmap-info-window
            :key="i"
            v-for="(m,i) in markers"
            :position="m.location"
            :opened="m.opened">
            <h2>{{m.name}}</h2>
          </gmap-info-window>
          <gmap-marker
            :key="i"
			      v-for="(m,i) in markers"
            :position="m.location"
			      @mouseover="m.opened=true"
			      @mouseout="m.opened=false">
          </gmap-marker>
        </gmap-map>
      </div>
    </template>
    <div class="footer padded">
      <div class="options" v-if="showmenu">
        <div class="menu-button first"><ui-icon>settings</ui-icon></div>
        <div class="menu-button"><ui-icon>mail_outline</ui-icon></div>
        <div class="menu-button"><ui-icon>date_range</ui-icon></div>
        <div class="menu-button" v-on:click="showMap()" ><ui-icon>map</ui-icon></div>
        <div class="menu-button"><ui-icon>list_black</ui-icon></div>
      </div>
      <div class="circle" >
        <div v-if="listview" v-on:click="showmenu = !showmenu">
          <ui-icon>menu</ui-icon>
        </div>
        <div v-if="detailedview || mapview" v-on:click="returnToListView()">
          <ui-icon>keyboard_arrow_left</ui-icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueResource from 'vue-resource'
  // import * as VueGoogleMaps from 'vue2-google-maps'
  import todolist from '../data/todolist'
  import { UiSelect, UiDatePicker, UiAutoComplete, UiIcon, UiButton } from 'keen-ui'

  Vue.use(VueResource)
  // Vue.use(VueGoogleMaps, {
  //   load: {
  //     key: 'AIzaSyAmgN4IZh9SILGetGtzplibnGXeuA3uu8o',
  //     libraries: 'places'
  //   }
  // })
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
        todolist,
        showmenu: false,
        listview: true,
        detailedview: false,
        detailedStepID: null,
        mapview: false,
        markers: [
          {
            opened: false,
            name: 'Bürgerbüro',
            location: {
              lat: 48.4693798,
              lng: 7.9433989
            }
          },
          {
            opened: false,
            name: 'Rathaus',
            location: {
              lat: 48.46943049999999,
              lng: 7.9427725
            }
          },
          {
            opened: false,
            name: 'Ausländerbüro',
            location: {
              lat: 48.469212,
              lng: 7.943698299999999
            }
          }
        ]
      }
    },
    methods: {
      showDetails (id) {
        this.listview = false
        this.detailedview = true
        this.mapview = false
        this.detailedStepID = id
        this.showmenu = false
      },
      returnToListView () {
        this.listview = true
        this.detailedview = false
        this.mapview = false
        this.detailedStepID = null
      },
      showMap () {
        this.listview = false
        this.detailedview = false
        this.mapview = true
        this.detailedStepID = null
      },
      loadTasks () {
        http.get('http://httpbin.org/get')
        .then(function (response) {
          // success
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
.main {
  padding-bottom: 120px; 
}
h1, h2 {
  font-weight: normal;
}
.header {
  color: #fff;
  height: 98px;
  background: #fcd37f ;
  background: -moz-linear-gradient(-45deg, #fcd37f 0%, #ea9b6c 29%, #d55757 63%, #d55757 100%);
  background: -webkit-linear-gradient(-45deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  background: linear-gradient(135deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcd37f ', endColorstr='#d55757 ',GradientType=1 );
}
.header h1 {
  font-size: 35px;
  font-weight: 900;
  padding-top: 10px;
}
.header img {
  padding-top: 6px;
}
.list {
  background: #fff;
}
.todo {
  margin-bottom: 4px;
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.22);
}
.todo, .todo * {
  cursor: pointer;
}
.todo:hover {
  background: #eee;
}
.todo .title h2 {
  padding-bottom: 10px;
  width: 270px;
}
.due {
  font-size: 13px;
  padding-right: 22px;
  padding-top: 10px;
  color: #C20A0A;
}
.todo label {
  display: block;
  padding-bottom: 2px;
}
.todo span label {
  display: inline;
}
label.mandatory {
  font-size: 13px;
  padding-right: 22px;
  padding-top: 10px;
  color: #C20A0A;
}
label.mandatory .ui-icon {
  font-size: 13px;
}
label.optional {
  font-size: 13px;
  padding-right: 22px;
  padding-top: 10px;
  color: #08732F;
}
label.optional .ui-icon {
  font-size: 13px;
}
.right {
  float: right;
}
.left {
  float: left;
}
.details {
  padding-left: 23px;
  padding-top: 14px;
}
.details .description {
  padding-top: 10px;
  padding-bottom: 10px;
}
.details .place-time {
  padding-top: 10px;
}
.details .place-time .place {
  display: block;
}
.details .place-time .date-time {
  display: block;
}
.details .place-time .date-time * {
  display: inline;
}
.details h2 {
  padding-top: 20px;
  font-weight: 900;
}
.status {
  font-size: 25px;
  padding-top: 35px;
  text-align: center;
}
.status .ui-icon {
  font-size: 30px;
}
.footer {
  background: #fcd37f ;
  background: -moz-linear-gradient(-45deg, #fcd37f 0%, #ea9b6c 29%, #d55757 63%, #d55757 100%);
  background: -webkit-linear-gradient(-45deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  background: linear-gradient(135deg, #fcd37f 0%,#ea9b6c 29%,#d55757 63%,#d55757 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcd37f ', endColorstr='#d55757 ',GradientType=1 );
  position: fixed; 
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  opacity: 0.90;
}
/* .footer .ui-icon {
  cursor: pointer;
} */
.padded {
  padding-left: 23px;
}
.padded-todo {
  padding-left: 23px;
  padding-top: 14px;
  padding-bottom: 20px;
}
.todo label{
  font-weight: 300;
}
.circle {
  border-radius: 50%;
  width: 58px;
  height: 58px;
  background: #f7C06C;
  color: #fff;
  position: fixed;
  bottom: 25px;
  left: 23px;
  opacity: 1;
  cursor: pointer;
}
.circle .ui-icon {
  padding: 9px;
  font-size: 40px;
}
.options {
  border-top-left-radius: 50px;
  border-bottom-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  width: 300px;
  height: 58px;
  background: #fff;
  position: fixed;
  bottom: 25px;
  left: 23px;
  color: #DE6628;
}
.slider:hover {
  transition: 1s;
  left: 0;
}
.options .menu-button.first {
  padding-left: 68px;
}
.options .menu-button {
  padding: 20px 10px;
  font-size: 40px;
  display: inline;
  cursor: pointer;
}

#map {
  width: 100%;
  height: calc(100vh - 148px);
  position: absolute;
  left:0;
  top:98;
}
</style>
