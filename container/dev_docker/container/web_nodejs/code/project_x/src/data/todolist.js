export default [
  {
    id: 1,
    title: 'Anmeldung des Wohnsitz',
    description: `Wenn Sie in eine andere Stadt oder Gemeinde ziehen, müssen Sie sich an Ihrem neuen Wohnsitz anmelden.

Zuständige Stelle
Stadt Offenburg Zentrales BürgerBüro Fischmarkt 2 77652 Offenburg
Tipp: Wenn der Zuzug in einen der Ortsteile von Offenburg erfolgt, kann die An- oder Ummeldung auch in den Ortsverwaltungen vorgenommen werden.
Verfahrensablauf

Um sich anzumelden, müssen Sie in der Regel persönlich bei der Meldebehörde erscheinen. Die Meldebehörde erfasst Ihre neuen Daten und legt Ihnen einen Ausdruck der Daten vor. Die Richtigkeit und Vollständigkeit Ihrer Daten bestätigen Sie mit Ihrer Unterschrift auf dem Ausdruck.

Sie können Ihre Familienangehörigen ebenfalls anmelden, wenn diese mit Ihnen bisher in der gleichen Wohnung gewohnt haben und mit Ihnen umziehen.
Nach der Anmeldung erhalten Sie eine Meldebestätigung für Ihre Unterlagen.

Erforderliche Unterlagen:
- Personalausweis
- Reisepass
- Ausweise der Familienangehörigen: Für Kinder, die keinen Kinderreisepass besitzen, müssen Sie die Geburtsurkunde vorlegen.
- Wohnungsgeberbestätigung seit 01.11.2015`,
    location: 'Bürger Büro',
    date: '09.11.2017',
    time: '08:00 am',
    due: '15.11.2017',
    mandatory: true,
    status: 1,
    dependency: {
      id: 0,
      title: 'Wohnungsgeberbestätigung',
      description: `Ihr Wohnungsgeber ist verpflichtet, Ihnen den Einzug in die neue Wohnung schriftlich zu bestätigen. Legen Sie diese Bescheinigung der Meldebehörde vor.
Falls diese noch nicht vom Wohnungsgeber ausgehändigt wurde, genügt zur Anmeldung auch der Mietvertrag. Die Wohnungsgeberbestätigung muss dann allerdings innerhalb von zwei Wochen dem BürgerBüro nachgereicht werden.
Zieht man als Eigentümerin oder Eigentümer selbst ein, gibt man die Wohnungsgeberbestätigung für sich selbst ab.
Ausnahmen
Keine Anmeldung ist erforderlich, wenn
man im Bundesgebiet bereits gemeldet ist und die Wohnung nicht länger als 6 Monate bezieht
man im Ausland wohnt und die Wohnung in Deutschland nicht länger als 3 Monate bezieht`,
      location: 'Home',
      date: '05.11.2017',
      time: '10:00 am',
      due: null,
      mandatory: true,
      status: 1
    },
    next: {
      id: 2,
      title: 'Ausländer Büro',
      description: `Das AusländerBüro ist zuständig für die im Stadtgebiet wohnenden Personen mit ausländischem Pass. 
Außerhalb des Stadtgebiets wenden Sie sich bitte an das Migrationsamt des Landratsamtes Ortenaukreis unter Tel. 0781 805-0.
Das AusländerBüro ist eines von fünf Sachgebieten des zentralen Bürgerbüros.

Zu unseren Aufgaben gehören:
Alles rund um Einreise und Aufenthalt von Ausländer/innen
Verpflichtungserklärungen für Gäste aus dem Ausland
Aufenthaltsrechtliche Betreuung von Asylbewerbern und Flüchtlingen
Ermöglichung der Teilnahme von Ausländer/innen an Integrationskursen
Öffnungszeiten:
Montag, Mittwoch, Freitag: 8 - 12 Uhr
Donnerstag: 8 - 18 Uhr
Dienstag nur nach Terminvereinbarung`,
      location: 'Ausländerbüro',
      date: '13.11.2017',
      time: '8:00 am',
      due: null,
      mandatory: true,
      status: 0
    }
  },
  {
    id: 3,
    title: 'Stromanbieter anmelden',
    description: `Informieren Sie sich unverbindlich über unsere Strom-Tarife oder werden Sie in wenigen Schritten unser Kunde.
https://www.e-werk-mittelbaden.de/privatkunden/Tarifrechner`,
    location: 'Home',
    date: '',
    time: '',
    due: null,
    mandatory: false,
    status: 0,
    dependency: {
      id: 0,
      title: 'Wohnungsgeberbestätigung',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris dignissim placerat sem et auctor. Maecenas et dictum sem. Nunc dapibus lobortis libero, nec consectetur magna vulputate vel. Praesent consectetur gravida augue quis scelerisque. Phasellus fringilla scelerisque leo ultricies hendrerit. Etiam sit amet rhoncus eros, in fringilla sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas consectetur tortor ac lacinia pellentesque. Pellentesque fermentum lectus sit amet consequat dictum. ',
      location: '',
      date: '',
      time: '',
      due: null,
      mandatory: false,
      status: 1
    }
  },
  {
    id: 4,
    title: 'Krankenversicherung',
    description: `Die Krankenkasse in Ihrer Nähe. Jetzt Mitglied bei der AOK werden!
https://www.aok.de/`,
    location: 'Home',
    date: '',
    time: '',
    due: null,
    mandatory: true,
    status: 1
  },
  {
    id: 5,
    title: 'Konto anlegen',
    description: `Von Altersvorsorge über Girokonto bis Versicherung: Privatkunden finden gute Beratung und Service bei der Volksbank in der Ortenau eG.

https://www.volksbank-ortenau.de/`,
    location: '',
    date: '',
    time: '',
    due: null,
    mandatory: true,
    status: 0
  },
  {
    id: 6,
    title: 'Weihnachtsmarkt',
    description: `Weihnachtsmarkt in der Offenburger Innenstadt, täglich von 11-21 Uhr.
Wenn der Offenburger Weihnachtsmarkt seine Pforten öffnet, hat sich die ganze Stadt vorweihnachtlich eingestimmt. Die Innenstadt liegt im Lichtglanz, Geschäfte haben Adventsschmuck angelegt und stimmen auf die besinnliche Zeit ein.

Auf dem Rathausplatz strahlt ein mit unzähligen Lichtern geschmückter Weihnachtsbaum, der wundervoll leuchtet.`,
    location: 'Offenburg Marktplatz',
    date: '28.11.2017 - 23.12.2017',
    time: '',
    due: null,
    mandatory: false,
    status: 0
  }
]
