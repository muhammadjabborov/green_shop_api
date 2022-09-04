from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices

from apps.shared.models import DeletedModel, BaseModel


class UserAddress(BaseModel, DeletedModel):
    class CountryChoices(TextChoices):



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
     'Falkland Islands (Malvinas)',
     'Faroe Islands',
     'Fiji',
     'Finland',
     'France',
     'French Guiana',
     'French Polynesia',
     'French Southern Territories',
     'Gabon',
     'Gambia',
     'Georgia',
     'Germany',
     'Ghana',
     'Gibraltar',
     'Greece',
     'Greenland',
     'Grenada',
     'Guadeloupe',
     'Guam',
     'Guatemala',
     'Guernsey',
     'Guinea',
     'Guinea-Bissau',
     'Guyana',
     'Haiti',
     'Heard Island and Mcdonald Islands',
     'Holy See (Vatican City State)',
     'Honduras',
     'Hong Kong',
     'Hungary',
     'Iceland',
     'India',
     'Indonesia',
     'Iran, Islamic Republic Of',
     'Iraq',
     'Ireland',
     'Isle of Man',
     'Israel',
     'Italy',
     'Jamaica',
     'Japan',
     'Jersey',
     'Jordan',
     'Kazakhstan',
     'Kenya',
     'Kiribati',
     'Korea, Democratic PeopleS Republic of',
     'Korea, Republic of',
     'Kuwait',
     'Kyrgyzstan',
     'Lao PeopleS Democratic Republic',
     'Latvia',
     'Lebanon',
     'Lesotho',
     'Liberia',
     'Libyan Arab Jamahiriya',
     'Liechtenstein',
     'Lithuania',
     'Luxembourg',
     'Macao',
     'Macedonia, The Former Yugoslav Republic of',
     'Madagascar',
     'Malawi',
     'Malaysia',
     'Maldives',
     'Mali',
     'Malta',
     'Marshall Islands',
     'Martinique',
     'Mauritania',
     'Mauritius',
     'Mayotte',
     'Mexico',
     'Micronesia, Federated States of',
     'Moldova, Republic of',
     'Monaco',
     'Mongolia',
     'Montserrat',
     'Morocco',
     'Mozambique',
     'Myanmar',
     'Namibia',
     'Nauru',
     'Nepal',
     'Netherlands',
     'Netherlands Antilles',
     'New Caledonia',
     'New Zealand',
     'Nicaragua',
     'Niger',
     'Nigeria',
     'Niue',
     'Norfolk Island',
     'Northern Mariana Islands',
     'Norway',
     'Oman',
     'Pakistan',
     'Palau',
     'Palestinian Territory, Occupied',
     'Panama',
     'Papua New Guinea',
     'Paraguay',
     'Peru',
     'Philippines',
     'Pitcairn',
     'Poland',
     'Portugal',
     'Puerto Rico',
     'Qatar',
     'Reunion',
     'Romania',
     'Russian Federation',
     'RWANDA',
     'Saint Helena',
     'Saint Kitts and Nevis',
     'Saint Lucia',
     'Saint Pierre and Miquelon',
     'Saint Vincent and the Grenadines',
     'Samoa',
     'San Marino',
     'Sao Tome and Principe',
     'Saudi Arabia',
     'Senegal',
     'Serbia and Montenegro',
     'Seychelles',
     'Sierra Leone',
     'Singapore',
     'Slovakia',
     'Slovenia',
     'Solomon Islands',
     'Somalia',
     'South Africa',
     'South Georgia and the South Sandwich Islands',
     'Spain',
     'Sri Lanka',
     'Sudan',
     'Suriname',
     'Svalbard and Jan Mayen',
     'Swaziland',
     'Sweden',
     'Switzerland',
     'Syrian Arab Republic',
     'Taiwan, Province of China',
     'Tajikistan',
     'Tanzania, United Republic of',
     'Thailand',
     'Timor-Leste',
     'Togo',
     'Tokelau',
     'Tonga',
     'Trinidad and Tobago',
     'Tunisia',
     'Turkey',
     'Turkmenistan',
     'Turks and Caicos Islands',
     'Tuvalu',
     'Uganda',
     'Ukraine',
     'United Arab Emirates',
     'United Kingdom',
     'United States',
     'United States Minor Outlying Islands',
     'Uruguay',
     'Uzbekistan',
     'Vanuatu',
     'Venezuela',
     'Viet Nam',
     'Virgin Islands, British',
     'Virgin Islands, U.S.',
     'Wallis and Futuna',
     'Western Sahara',
     'Yemen',
     'Zambia',
     'Zimbabwe'


    AF = 'Afghanistan',
    AX = 'Åland Islands',
    AL =  'Albania',
    DZ = 'Algeria',
    AS =  'American Samoa',
    AD = 'AndorrA',
    AO =  'Angola',
    AI =  'Anguilla',
    AQ = 'Antarctica',
    AG = 'Antigua and Barbuda',
    AR = 'Argentina',
    AM = 'Armenia',
    AW = 'Aruba',
    AU = 'Australia',
    AT = 'Austria',
    AZ =  'Azerbaijan',
    BS =  'Bahamas',
    BH =  'Bahrain',
    BD = 'Bangladesh',
    BB =   'Barbados',
    BY = 'Belarus',
    BE = 'Belgium',
    BZ =  'Belize',
    BJ = 'Benin',
    BM = 'Bermuda',
    BT = 'Bhutan',
    BO = 'Bolivia',
    BA = 'Bosnia and Herzegovina',
    BW = 'Botswana',
    BV = 'Bouvet Island',
    BR =  'Brazil',
    IO ='British Indian Ocean Territory',
    BN = 'Brunei Darussalam',
    BG = 'Bulgaria',
    BF = 'Burkina Faso',
    BI = 'Burundi',
    KH = 'Cambodia',
    CM = 'Cameroon',
    CA = 'Canada',
    CV = 'Cape Verde',
    KY = 'Cayman Islands',
    CF = 'Central African Republic',
    TD = 'Chad',
    CL = 'Chile',
    CN = 'China',
    CX =  'Christmas Island',
    CC = 'Cocos (Keeling) Islands',
    CO = 'Colombia',
    KM =  'Comoros',
    CG = 'Congo',
    CD = 'Congo',
    CK = 'Cook Islands',
    CR =   'Costa Rica',
    CI = 'Cote DIvoire',
    HR = 'Croatia',
    CY = 'Cyprus',
    CZ =  'Czech Republic',
    DK =
    DJ =
    DM =
    DO =
    EC =
    EG =
    SV =
    GQ =
    ER =
    EE =
    ET =
    FK =
    FO =
    FJ =
    FI =
    FR =
    GF =
    PF =
    TF =
    GA =
    GM =
    GE =
    DE =
    GH =
    GI =
    GR =
    GL =
    GD =
    GP =
    GU =
    GT =
    GG =
    GN =
    GW =
    GY =
    HT =
    HM =
    VA =
    HN =
    HK =
    HU =
    IS =
    IN =
    ID =
    IR =
    IQ =
    IE =
    IM =
    IL =
    IT =
    JM =
    JP =
    JE =
    JO =
    KZ =
    KE =
    KI =
    KP =
    KR =
    KW =
    KG =
    LA =
    LV =
    LB =
    LS =
    LR =
    LY =
    LI =
    LT =
    LU =
    MO =
    MK =
    MG =
    MW =
    MY =
    MV =
    ML =
    MT =
    MH =
    MQ =
    MR =
    MU =
    YT =
    MX =
    FM =
    MD =
    MC =
    MN =
    MS =
    MA =
    MZ =
    MM =
    NA =
    NR =
    NP =
    NL =
    AN =
    NC =
    NZ =
    NI =
    NE =
    NG =
    NU =
    NF =
    MP =
    NO =
    OM =
    PK =
    PW =
    PS =
    PA =
    PG =
    PY =
    PE =
    PH =
    PN =
    PL =
    PT =
    PR =
    QA =
    RE =
    RO =
    RU =
    RW =
    SH =
    KN =
    LC =
    PM =
    VC =
    WS =
    SM =
    ST =
    SA =
    SN =
    CS =
    SC =
    SL =
    SG =
    SK =
    SI =
    SB =
    SO =
    ZA =
    GS =
    ES =
    LK =
    SD =
    SR =
    SJ =
    SZ =
    SE =
    CH =
    SY =
    TW =
    TJ =
    TZ =
    TH =
    TL =
    TG =
    TK =
    TO =
    TT =
    TN =
    TR =
    TM =
    TC =
    TV =
    UG =
    UA =
    AE =
    GB =
    US =
    UM =
    UY =
    UZ =
    VU =
    VE =
    VN =
    VG =
    VI =
    WF =
    EH =
    YE =
    ZM =
    ZW =
    first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        country_region = models.CharField(max_length=25, choices=CountryChoices.choices, default=CountryChoices.UZB)
        city = models.CharField(max_length=25)
        zip_code = models.CharField(max_length=6)
        # email = models.ForeignKey(User, on_delete=models.CASCADE)
        number = models.CharField(max_length=25)
