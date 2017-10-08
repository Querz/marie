drop table hackathon.cities;
drop table hackathon.steps;
drop table hackathon.profile_steps;
drop table hackathon.step_tags;
drop table hackathon.profiles;
drop table hackathon.move_reasons;

create database if not exists hackathon;

use hackathon;

create table if not exists cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location_lat DOUBLE,
    location_lng DOUBLE,
    buildings TEXT
);

create table if not exists steps (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    location_lat DOUBLE,
    location_lng DOUBLE,
    description TEXT,
    title TEXT,
    child INT,
    dependency INT,
    mandatory INT(8),
    location_name TEXT
);

create table if not exists profile_steps (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    profile INT,
    date DATE,
    due DATE,
    time VARCHAR(5),
    status INT(8)
);

create table if not exists step_tags (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    tag INT(8)
);

create table if not exists profiles (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    language INT(8),
    age INT,
    children INT,
    new_residence VARCHAR(100),
    new_residence_lower VARCHAR(100),
    nationality CHAR(2),
    move_date DATE
);

create table if not exists move_reasons (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    profile INT,
    reason INT(8)
);

insert into cities (name, location_lat, location_lng)
values ('Offenburg', 48.46943049999999, 7.9427725);

insert into cities (name, location_lat, location_lng)
values ('Kehl', 48.5637447, 7.8039819)

insert into profiles (new_residence, new_residence_lower, state_of_work, nationality, password, children, name, language, age, move_date, email)
values ('Offenburg', 'offenburg', 0, 'AE', 'secret', 0, 'Moataz Rizk', 1, 25, '2017-10-10', 'mor@vioma.de');

insert into profiles (new_residence, new_residence_lower, state_of_work, nationality, password, children, name, language, age, move_date, email)
values ('Kehl', 'kehl', 0, 'DE', 'secret', 0, 'Raphael Boes', 1, 23, '2017-10-25', 'rb@vioma.de');

insert into move_reasons (profile, reason)
value (1, 0), ((select id from profiles where email = 'mor@vioma.de'), 1);

insert into move_reasons (profile, reason)
value (2, 2);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (1, 'Offenburg', 48.4693833, 7.9412102, 'Wenn Sie in eine andere Stadt oder Gemeinde ziehen, muessen Sie sich an Ihrem neuen Wohnsitz anmelden.\n\nZustaendige Stelle\nStadt Offenburg Zentrales BuergerBuero Fischmarkt 2 77652 Offenburg\nTipp: Wenn der Zuzug in einen der Ortsteile von Offenburg erfolgt, kann die An- oder Ummeldung auch in den Ortsverwaltungen vorgenommen werden.\nVerfahrensablauf\n\nUm sich anzumelden, muessen Sie in der Regel persoenlich bei der Meldebehoerde erscheinen. Die Meldebehoerde erfasst Ihre neuen Daten und legt Ihnen einen Ausdruck der Daten vor. Die Richtigkeit und Vollstaendigkeit Ihrer Daten bestaetigen Sie mit Ihrer Unterschrift auf dem Ausdruck.\n\nSie koennen Ihre Familienangehoerigen ebenfalls anmelden, wenn diese mit Ihnen bisher in der gleichen Wohnung gewohnt haben und mit Ihnen umziehen.\nNach der Anmeldung erhalten Sie eine Meldebestaetigung fuer Ihre Unterlagen.\n\nErforderliche Unterlagen:\n- Personalausweis\n- Reisepass\n- Ausweise der Familienangehoerigen: Fuer Kinder, die keinen Kinderreisepass besitzen, muessen Sie die Geburtsurkunde vorlegen.\n- Wohnungsgeberbestaetigung seit 01.11.2015', 'Anmeldung / Ummeldung des Wohnsitz', 3, 2, 1, 'Buergerbuero');

insert into step_tags (step, tag)
values (1, 8), (1, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (1, 1, '2017-09-11', '2017-11-15', '08:00', 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (2, 'Offenburg', 48.4693833, 7.9412102, 'Ihr Wohnungsgeber ist verpflichtet, Ihnen den Einzug in die neue Wohnung schriftlich zu bestaetigen. Legen Sie diese Bescheinigung der Meldebehoerde vor.\nFalls diese noch nicht vom Wohnungsgeber ausgehaendigt wurde, genuegt zur Anmeldung auch der Mietvertrag. Die Wohnungsgeberbestaetigung muss dann allerdings innerhalb von zwei Wochen dem BuergerBuero nachgereicht werden.\nZieht man als Eigentuemerin oder Eigentuemer selbst ein, gibt man die Wohnungsgeberbestaetigung fuer sich selbst ab.\nAusnahmen\nKeine Anmeldung ist erforderlich, wenn\nman im Bundesgebiet bereits gemeldet ist und die Wohnung nicht laenger als 6 Monate bezieht\nman im Ausland wohnt und die Wohnung in Deutschland nicht laenger als 3 Monate bezieht', 'Wohnungsgeberbestaetigung', NULL, 1, 1, 'Buergerbuero');

insert into step_tags (step, tag)
values (2, 8), (2, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (2, 1, '2017-05-11', NULL, NULL, 1);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (3, 'Offenburg', 48.4692155, 7.9415096, 'Das AuslaenderBuero ist zustaendig fuer die im Stadtgebiet wohnenden Personen mit auslaendischem Pass. \nAusserhalb des Stadtgebiets wenden Sie sich bitte an das Migrationsamt des Landratsamtes Ortenaukreis unter Tel. 0781 805-0.\nDas AuslaenderBuero ist eines von fuenf Sachgebieten des zentralen Buergerbueros.\n\nZu unseren Aufgaben gehoeren:\nAlles rund um Einreise und Aufenthalt von Auslaender/innen\nVerpflichtungserklaerungen fuer Gaeste aus dem Ausland\nAufenthaltsrechtliche Betreuung von Asylbewerbern und Fluechtlingen\nErmoeglichung der Teilnahme von Auslaender/innen an Integrationskursen\noeffnungszeiten:\nMontag, Mittwoch, Freitag: 8 - 12 Uhr\nDonnerstag: 8 - 18 Uhr\nDienstag nur nach Terminvereinbarung', 'Auslaenderbuero', NULL, NULL, 1, 'Auslaenderbuero');

insert into step_tags (step, tag)
values (3, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (3, 1, '2017-11-13', NULL, '08:00', 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (4, 'Offenburg', 0.0, 0.0, 'Informieren Sie sich unverbindlich ueber unsere Strom-Tarife oder werden Sie in wenigen Schritten unser Kunde.\nhttps://www.e-werk-mittelbaden.de/privatkunden/Tarifrechner', 'Home', NULL, 1, 0, 'Home');

insert into step_tags (step, tag)
values (4, 8), (4, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (4, 1, NULL, NULL, NULL, 1);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (5, 'Offenburg', 48.4643584, 7.9251311, 'Die Krankenkasse in Ihrer Nähe. Jetzt Mitglied bei der AOK werden!\nhttps://www.aok.de/', 'Krankenversicherung', NULL, NULL, 1, 'AOK Offenburg');

insert into step_tags (step, tag)
values (5, 8), (5, 9), (5, 2), (5, 7);

insert into profile_steps (step, profile, date, due, time, status)
values (5, 1, NULL, NULL, NULL, 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (6, 'Offenburg', 48.4643584, 7.9251311, 'Weihnachtsmarkt in der Offenburger Innenstadt, taeglich von 11-21 Uhr.\nWenn der Offenburger Weihnachtsmarkt seine Pforten oeffnet, hat sich die ganze Stadt vorweihnachtlich eingestimmt. Die Innenstadt liegt im Lichtglanz, Geschaefte haben Adventsschmuck angelegt und stimmen auf die besinnliche Zeit ein.\n\nAuf dem Rathausplatz strahlt ein mit unzaehligen Lichtern geschmueckter Weihnachtsbaum, der wundervoll leuchtet.', 'Weihnachtsmarkt', NULL, NULL, 0, 'Marktplatz');

insert into step_tags (step, tag)
values (6, 4), (6, 7);

insert into profile_steps (step, profile, date, due, time, status)
values (6, 1, '2017-12-10', '2017-12-26', '11:00', 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (7, 'Offenburg', 48.4693833, 7.9412102, 'Beim Buergerbuero liegen Gelbe Saecke aus - Sollten Sie welche benoetigen, greifen Sie zu.\n\nGelbe Saecke werden auch monatlich direkt zu Ihnen nach Hause geliefert.', 'Gelber Sack', NULL, NULL, 0, 'Buergerbuero');

insert into step_tags (step, tag)
values (7, 8), (7, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (7, 1, NULL, NULL, NULL, 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (8, 'Offenburg', 48.4625052, 7.936347, 'Das Freizeitbad Stegermatt steht Ihnen nd Ihrer Familie in Offenburg zur verfuegung; Ob Sie Ihrer Gesundheit etwas Gutes tun oder einfach nur entspannen wollen - Im Freizeitbad Stegermatt koennen Sie beides zugleich tun.', 'Schwimmbad', NULL, NULL, 0, 'Freizeitbad Stegermatt');

insert into step_tags (step, tag)
values (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7);

insert into profile_steps (step, profile, date, due, time, status)
values (8, 1, NULL, NULL, NULL, 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (9, 'Kehl', 48.5721349, 7.7433326, 'Wenn Sie in eine andere Stadt oder Gemeinde ziehen, muessen Sie sich an Ihrem neuen Wohnsitz anmelden.\n\nZustaendige Stelle\nStadt Offenburg Zentrales BuergerBuero Fischmarkt 2 77652 Offenburg\nTipp: Wenn der Zuzug in einen der Ortsteile von Offenburg erfolgt, kann die An- oder Ummeldung auch in den Ortsverwaltungen vorgenommen werden.\nVerfahrensablauf\n\nUm sich anzumelden, muessen Sie in der Regel persoenlich bei der Meldebehoerde erscheinen. Die Meldebehoerde erfasst Ihre neuen Daten und legt Ihnen einen Ausdruck der Daten vor. Die Richtigkeit und Vollstaendigkeit Ihrer Daten bestaetigen Sie mit Ihrer Unterschrift auf dem Ausdruck.\n\nSie koennen Ihre Familienangehoerigen ebenfalls anmelden, wenn diese mit Ihnen bisher in der gleichen Wohnung gewohnt haben und mit Ihnen umziehen.\nNach der Anmeldung erhalten Sie eine Meldebestaetigung fuer Ihre Unterlagen.\n\nErforderliche Unterlagen:\n- Personalausweis\n- Reisepass\n- Ausweise der Familienangehoerigen: Fuer Kinder, die keinen Kinderreisepass besitzen, muessen Sie die Geburtsurkunde vorlegen.\n- Wohnungsgeberbestaetigung seit 01.11.2015', 'Anmeldung / Ummeldung des Wohnsitz', 11, 10, 1, 'Rathaus');

insert into step_tags (step, tag)
values (9, 8), (9, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (9, 1, '2017-09-11', '2017-11-15', '08:00', 0);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (10, 'Kehl', 48.5721349, 7.7433326, 'Ihr Wohnungsgeber ist verpflichtet, Ihnen den Einzug in die neue Wohnung schriftlich zu bestaetigen. Legen Sie diese Bescheinigung der Meldebehoerde vor.\nFalls diese noch nicht vom Wohnungsgeber ausgehaendigt wurde, genuegt zur Anmeldung auch der Mietvertrag. Die Wohnungsgeberbestaetigung muss dann allerdings innerhalb von zwei Wochen dem BuergerBuero nachgereicht werden.\nZieht man als Eigentuemerin oder Eigentuemer selbst ein, gibt man die Wohnungsgeberbestaetigung fuer sich selbst ab.\nAusnahmen\nKeine Anmeldung ist erforderlich, wenn\nman im Bundesgebiet bereits gemeldet ist und die Wohnung nicht laenger als 6 Monate bezieht\nman im Ausland wohnt und die Wohnung in Deutschland nicht laenger als 3 Monate bezieht', 'Wohnungsgeberbestaetigung', NULL, 9, 1, 'Rathaus');

insert into step_tags (step, tag)
values (10, 8), (10, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (10, 1, '2017-05-11', NULL, NULL, 1);
--
insert into steps (id, city, location_lat, location_lng, description, title, child, dependency, mandatory, location_name)
values (11, 'Kehl', 48.469212, 7.9349436, 'Das AuslaenderBuero ist zustaendig fuer die im Stadtgebiet wohnenden Personen mit auslaendischem Pass. \nAusserhalb des Stadtgebiets wenden Sie sich bitte an das Migrationsamt des Landratsamtes Ortenaukreis unter Tel. 0781 805-0.\nDas AuslaenderBuero ist eines von fuenf Sachgebieten des zentralen Buergerbueros.\n\nZu unseren Aufgaben gehoeren:\nAlles rund um Einreise und Aufenthalt von Auslaender/innen\nVerpflichtungserklaerungen fuer Gaeste aus dem Ausland\nAufenthaltsrechtliche Betreuung von Asylbewerbern und Fluechtlingen\nErmoeglichung der Teilnahme von Auslaender/innen an Integrationskursen\noeffnungszeiten:\nMontag, Mittwoch, Freitag: 8 - 12 Uhr\nDonnerstag: 8 - 18 Uhr\nDienstag nur nach Terminvereinbarung', 'Auslaenderbuero', NULL, NULL, 1, 'Auslaenderbuero');

insert into step_tags (step, tag)
values (11, 9);

insert into profile_steps (step, profile, date, due, time, status)
values (11, 1, '2017-11-13', NULL, '08:00', 0);