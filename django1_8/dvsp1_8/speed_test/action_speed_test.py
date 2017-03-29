import random

from speed_test.models import Title, Contact, Country
from django.db import transaction
from profilehooks import profile


class ActionSpeedTest(object):

    @profile(filename='django1_8.prof')
    def __init__(self, number_of_actions):
        self.forenames = ['Fred',
                          'Bill',
                          'Gary',
                          'Mary',
                          'Tiny',
                          'Emma',
                          'Gemma',
                          'William',
                          'Tom',
                          'Dave',
                          'Julie',
                          'Daniel',
                          'James',
                          'Mark',
                          'Ben',
                          'John',
                          'Graham']
        self.surnames = ['Blogs',
                         'Williams',
                         'Turner',
                         'Moore',
                         'Whitehead',
                         'Willmore',
                         'Dennis',
                         'Berry',
                         'Trask']

        self.titles = ['Mr',
                       'Mrs',
                       'Ms.',
                       'Dr',
                       'Rev',
                       'Lady',
                       'Sir']

        self.countries = [
            'Afghanistan',
            'Albania',
            'Algeria',
            'Andorra',
            'Angola',
            'Antigua and Barbuda',
            'Argentina',
            'Armenia',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bahrain',
            'Bangladesh',
            'Barbados',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bhutan',
            'Bolivia',
            'Bosnia and Herzegovina',
            'Botswana',
            'Brazil',
            'Brunei Darussalam',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cabo Verde',
            'Cambodia',
            'Cameroon',
            'Canada',
            'Central African Republic',
            'Chad',
            'Chile',
            'China',
            'Colombia',
            'Comoros',
            'Congo',
            'Costa Rica',
            'Cote d\'Ivoire',
            'Croatia',
            'Cuba',
            'Cyprus',
            'Czech Republic',
            'Democratic People\'s Republic of Korea (North Korea)',
            'Democratic Republic of the Cong',
            'Denmark',
            'Djibouti',
            'Dominica',
            'Dominican Republic',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Eritrea',
            'Estonia',
            'Ethiopia',
            'Fiji',
            'Finland',
            'France',
            'Gabon',
            'Gambia',
            'Georgia',
            'Germany',
            'Ghana',
            'Greece',
            'Grenada',
            'Guatemala',
            'Guinea',
            'Guinea-Bissau',
            'Guyana',
            'Haiti',
            'Honduras',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Ireland',
            'Israel',
            'Italy',
            'Jamaica',
            'Japan',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Kiribati',
            'Kuwait',
            'Kyrgyzstan',
            'Lao People\'s Democratic Republic (Laos)',
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Maldives',
            'Mali',
            'Malta',
            'Marshall Islands',
            'Mauritania',
            'Mauritius',
            'Mexico',
            'Micronesia (Federated States of)',
            'Monaco',
            'Mongolia',
            'Montenegro',
            'Morocco',
            'Mozambique',
            'Myanmar',
            'Namibia',
            'Nauru',
            'Nepal',
            'Netherlands',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'Norway',
            'Oman',
            'Pakistan',
            'Palau',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Poland',
            'Portugal',
            'Qatar',
            'Republic of Korea (South Korea)',
            'Republic of Moldova',
            'Romania',
            'Russian Federation',
            'Rwanda',
            'Saint Kitts and Nevis',
            'Saint Lucia',
            'Saint Vincent and the Grenadines',
            'Samoa',
            'San Marino',
            'Sao Tome and Principe',
            'Saudi Arabia',
            'Senegal',
            'Serbia',
            'Seychelles',
            'Sierra Leone',
            'Singapore',
            'Slovakia',
            'Slovenia',
            'Solomon Islands',
            'Somalia',
            'South Africa',
            'South Sudan',
            'Spain',
            'Sri Lanka',
            'Sudan',
            'Suriname',
            'Swaziland',
            'Sweden',
            'Switzerland',
            'Syrian Arab Republic',
            'Tajikistan',
            'Thailand',
            'Timor-Leste',
            'Togo',
            'Tonga',
            'Trinidad and Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'Tuvalu',
            'Uganda',
            'Ukraine',
            'United Arab Emirates',
            'United Kingdom of Great Britain and Northern Ireland',
            'United Republic of Tanzania',
            'United States of America',
            'Uruguay',
            'Uzbekistan',
            'Vanuatu',
            'Venezuela',
            'Vietnam',
            'Yemen',
            'Zambia',
            'Zimbabwe'
        ]

        self.number_of_actions = number_of_actions
        self.forenames_len = len(self.forenames)
        self.surnames_len = len(self.surnames)
        self.titles_len = len(self.titles)
        self.countries_len = len(self.countries)
        self.random = random
        self.titles_obj = []
        self.countries_obj = []
        self.setup_titles()
        self.setup_countries()

        self.test_insert()
        self.test_insert_transaction()
        self.test_update()
        self.test_update_transaction()
        self.test_no_select_related()
        self.test_select_related()
        self.test_no_prefetch_related()
        self.test_prefetch_related()

    def setup_titles(self):
        self.print_line('setup_titles')
        for title in self.titles:
            t = Title(title=title)
            t.save()
            self.titles_obj.append(t)

    def setup_countries(self):
        self.print_line('setup_countries')
        for country in self.countries:
            c = Country(name=country)
            c.save()
            self.countries_obj.append(c)

    def test_insert(self):
        self.print_line('test_insert')
        self.random.seed('test_insert')
        for index in range(0, self.number_of_actions):
            contact = Contact()
            contact.type = 1

            contact.title = self.titles_obj[self.random.randrange(0, self.titles_len-1)]
            contact.country = self.countries_obj[self.random.randrange(0, self.countries_len - 1)]
            contact.forename = self.forenames[self.random.randrange(0, self.forenames_len-1)]
            contact.surnames = self.forenames[self.random.randrange(0, self.surnames_len-1)]
            contact.save()

    def test_insert_transaction(self):
        self.print_line('test_insert_transaction')
        with transaction.atomic():
            self.random.seed('test_insert')
            for index in range(0, self.number_of_actions):
                contact = Contact()
                contact.type = 2
                contact.title = self.titles_obj[self.random.randrange(0, self.titles_len-1)]
                contact.country = self.countries_obj[self.random.randrange(0, self.countries_len - 1)]
                contact.forename = self.forenames[self.random.randrange(0, self.forenames_len-1)]
                contact.surnames = self.forenames[self.random.randrange(0, self.surnames_len-1)]
                contact.save()

    def test_update(self):
        self.print_line('test_update')
        self.random.seed('test_update')

        contact_ids = []
        for contact in Contact.objects.filter(type=1, forename='Tom'):
            contact_ids.append(contact.id)

        for contact_id in contact_ids:
            contact = Contact.objects.get(id=contact_id)
            contact.title = self.titles_obj[self.random.randrange(0, self.titles_len - 1)]
            contact.country = self.countries_obj[self.random.randrange(0, self.countries_len - 1)]
            contact.forename = self.forenames[self.random.randrange(0, self.forenames_len - 1)]
            contact.surnames = self.forenames[self.random.randrange(0, self.surnames_len - 1)]
            contact.save()

    def test_update_transaction(self):
        self.print_line('test_update_transaction')
        self.random.seed('test_update')

        contact_ids = []
        for contact in Contact.objects.filter(type=2, forename='Tom'):
            contact_ids.append(contact.id)

        with transaction.atomic():
            for contact_id in contact_ids:
                contact = Contact.objects.get(id=contact_id)
                contact.title = self.titles_obj[self.random.randrange(0, self.titles_len - 1)]
                contact.country = self.countries_obj[self.random.randrange(0, self.countries_len - 1)]
                contact.forename = self.forenames[self.random.randrange(0, self.forenames_len - 1)]
                contact.surnames = self.forenames[self.random.randrange(0, self.surnames_len - 1)]
                contact.save()

    def test_no_select_related(self):
        self.print_line('test_no_select_related')
        for contact in Contact.objects.all():
            self.print_contact(contact)

    def test_select_related(self):
        self.print_line('test_select_related')
        for contact in Contact.objects.select_related('title', 'country').all():
            self.print_contact(contact)

    def test_no_prefetch_related(self):
        self.print_line('test_no_prefetch_related')
        for country in Country.objects.all():
            for contact in country.contact_set.all():
                self.print_name(contact)

    def test_prefetch_related(self):
        self.print_line('test_prefetch_related')
        for country in Country.objects.all().prefetch_related('contact_set'):
            for contact in country.contact_set.all():
                self.print_name(contact)

    @staticmethod
    def print_contact(contact):
        print("%s %s %s in %s" % (contact.title.title, contact.forename, contact.surname, contact.country.name))

    @staticmethod
    def print_name(contact):
        print("%s %s" % (contact.forename, contact.surname))

    def print_line(self, name):
        print("\033[94m%s\033[0m" % name)
