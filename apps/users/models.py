from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.core.validators import MaxValueValidator, MinValueValidator, integer_validator
from django.db import models
from django.db.models import TextChoices, ForeignKey, CASCADE, ImageField, IntegerField
import os

from apps.shared.models import DeletedModel, BaseModel


class UserImage(BaseModel, DeletedModel):
    user = ForeignKey(User, CASCADE, related_name='user_image')
    image = ImageField(upload_to='user-images/', default='media/images/avatar.png')


class UserAddress(BaseModel, DeletedModel):
    class CountryChoices(TextChoices):
        AF = "Afghanistan",
        AX = "Åland Islands",
        AL = "Albania",
        DZ = "Algeria",
        AS = "American Samoa",
        AD = "Andorra",
        AO = "Angola",
        AI = "Anguilla",
        AQ = "Antarctica",
        AG = "Antigua and Barbuda",
        AR = "Argentina",
        AM = "Armenia",
        AW = "Aruba",
        AU = "Australia",
        AT = "Austria",
        AZ = "Azerbaijan",
        BS = "Bahamas (the)",
        BH = "Bahrain",
        BD = "Bangladesh",
        BB = "Barbados",
        BY = "Belarus",
        BE = "Belgium",
        BZ = "Belize",
        BJ = "Benin",
        BM = "Bermuda",
        BT = "Bhutan",
        BO = "Bolivia (Plurinational State of)",
        BA = "Bonaire, Sint Eustatius and Saba",
        BW = "Bosnia and Herzegovina",
        BV = "Botswana",
        BR = "Bouvet Island",
        IO = "Brazil",
        BN = "British Indian Ocean Territory (the)",
        BG = "Brunei Darussalam",
        BF = "Bulgaria",
        BI = "Burkina Faso",
        KH = "Burundi",
        CM = "Cabo Verde",
        CA = "Cambodia",
        CV = "Cameroon",
        KY = "Canada",
        CF = "Cayman Islands (the)",
        TD = "Central African Republic (the)",
        CL = "Chad",
        CN = "Chile",
        CX = "China",
        CC = "Christmas Island",
        CO = "Cocos (Keeling) Islands (the)",
        KM = "Colombia",
        CG = "Comoros (the)",
        CD = "Congo (the Democratic Republic of the)",
        CK = "Congo (the)",
        CR = "Cook Islands (the)",
        CI = "Costa Rica",
        HR = "Croatia",
        CU = "Cuba",
        CY = "Curaçao",
        CZ = "Cyprus",
        DK = "Czechia",
        DJ = "Côte d'Ivoire",
        DM = "Denmark",
        DO = "Djibouti",
        EC = "Dominica",
        EG = "Dominican Republic (the)",
        SV = "Ecuador",
        GQ = "Egypt",
        ER = "El Salvador",
        EE = "Equatorial Guinea",
        ET = "Eritrea",
        FK = "Estonia",
        FO = "Eswatini",
        FJ = "Ethiopia",
        FI = "Falkland Islands (the) [Malvinas]",
        FR = "Faroe Islands (the)",
        GF = "Fiji",
        PF = "Finland",
        TF = "France",
        GA = "French Guiana",
        GM = "French Polynesia",
        GE = "French Southern Territories (the)",
        DE = "Gabon",
        GH = "Gambia (the)",
        GI = "Georgia",
        GR = "Germany",
        GL = "Ghana",
        GD = "Gibraltar",
        GP = "Greece",
        GU = "Greenland",
        GT = "Grenada",
        GG = "Guadeloupe",
        GN = "Guam",
        GW = "Guatemala",
        GY = "Guernsey",
        HT = "Guinea",
        HM = "Guinea-Bissau",
        VA = "Guyana",
        HN = "Haiti",
        HK = "Heard Island and McDonald Islands",
        HU = "Holy See (the)",
        IS = "Honduras",
        IN = "Hong Kong",
        ID = "Hungary",
        IR = "Iceland",
        IQ = "India",
        IE = "Indonesia",
        IM = "Iran (Islamic Republic of)",
        IL = "Iraq",
        IT = "Ireland",
        JM = "Isle of Man",
        JP = "Israel",
        JE = "Italy",
        JO = "Jamaica",
        KZ = "Japan",
        KE = "Jersey",
        KI = "Jordan",
        KP = "Kazakhstan",
        KR = "Kenya",
        KW = "Kiribati",
        KG = "Korea (the Democratic People's Republic of)",
        LA = "Korea (the Republic of)",
        LV = "Kuwait",
        LB = "Kyrgyzstan",
        LS = "Lao People's Democratic Republic (the)",
        LR = "Latvia",
        LY = "Lebanon",
        LI = "Lesotho",
        LT = "Liberia",
        LU = "Libya",
        MO = "Liechtenstein",
        MK = "Lithuania",
        MG = "Luxembourg",
        MW = "Macao",
        MY = "Madagascar",
        MV = "Malawi",
        ML = "Malaysia",
        MT = "Maldives",
        MH = "Mali",
        MQ = "Malta",
        MR = "Marshall Islands (the)",
        MU = "Martinique",
        YT = "Mauritania",
        MX = "Mauritius",
        FM = "Mayotte",
        MD = "Mexico",
        MC = "Micronesia (Federated States of)",
        MN = "Moldova (the Republic of)",
        MS = "Monaco",
        MA = "Mongolia",
        MZ = "Montenegro",
        MM = "Montserrat",
        NA = "Morocco",
        NR = "Mozambique",
        NP = "Myanmar",
        NL = "Namibia",
        AN = "Nauru",
        NC = "Nepal",
        NZ = "Netherlands (the)",
        NI = "New Caledonia",
        NE = "New Zealand",
        NG = "Nicaragua",
        NU = "Niger (the)",
        NF = "Nigeria",
        MP = "Niue",
        NO = "Norfolk Island",
        OM = "Northern Mariana Islands (the)",
        PK = "Norway",
        PW = "Oman",
        PS = "Pakistan",
        PA = "Palau",
        PG = "Palestine, State of",
        PY = "Panama",
        PE = "Papua New Guinea",
        PH = "Paraguay",
        PN = "Peru",
        PL = "Philippines (the)",
        PT = "Pitcairn",
        PR = "Poland",
        QA = "Portugal",
        RE = "Puerto Rico",
        RO = "Qatar",
        RU = "Republic of North Macedonia",
        RW = "Romania",
        SH = "Russian Federation (the)",
        KN = "Rwanda",
        LC = "Réunion",
        PM = "Saint Barthélemy",
        VC = "Saint Helena, Ascension and Tristan da Cunha",
        WS = "Saint Kitts and Nevis",
        SM = "Saint Lucia",
        ST = "Saint Martin (French part)",
        SA = "Saint Pierre and Miquelon",
        SN = "Saint Vincent and the Grenadines",
        CS = "Samoa",
        SC = "San Marino",
        SL = "Sao Tome and Principe",
        SG = "Saudi Arabia",
        SK = "Senegal",
        SI = "Serbia",
        SB = "Seychelles",
        SO = "Sierra Leone",
        ZA = "Singapore",
        GS = "Sint Maarten (Dutch part)",
        ES = "Slovakia",
        LK = "Slovenia",
        SD = "Solomon Islands",
        SR = "Somalia",
        SJ = "South Africa",
        SZ = "South Georgia and the South Sandwich Islands",
        SE = "South Sudan",
        CH = "Spain",
        SY = "Sri Lanka",
        TW = "Sudan (the)",
        TJ = "Suriname",
        TZ = "Svalbard and Jan Mayen",
        TH = "Sweden",
        TL = "Switzerland",
        TG = "Syrian Arab Republic",
        TK = "Taiwan (Province of China)",
        TO = "Tajikistan",
        TT = "Tanzania, United Republic of",
        TN = "Thailand",
        TR = "Timor-Leste",
        TM = "Togo",
        TC = "Tokelau",
        TV = "Tonga",
        UG = "Trinidad and Tobago",
        UA = "Tunisia",
        AE = "Turkey",
        GB = "Turkmenistan",
        US = "Turks and Caicos Islands (the)",
        UM = "Tuvalu",
        UY = "Uganda",
        UZ = "Ukraine",
        VU = "United Arab Emirates (the)",
        VE = "United Kingdom of Great Britain and Northern Ireland (the)",
        VN = "United States Minor Outlying Islands (the)",
        VG = "United States of America (the)",
        VI = "Uruguay",
        WF = "Uzbekistan",
        EH = "Vanuatu",
        YE = "Venezuela (Bolivarian Republic of)",
        ZM = "Viet Nam",
        ZW = "Zimbabwe"


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_region = models.CharField(max_length=255, choices=CountryChoices.choices, default=CountryChoices.UZ)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=6)
