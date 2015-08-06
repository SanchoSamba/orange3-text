"""Country names to ISO3166_alpha2 codes mapping

Roughly generated by the following bash script on GNU/Linux:

    while read cc name; do
        [ ! "$cc" ] &&
            continue
        out=$(isoquery $cc | cut -f3 --complement);
        [ ! "$out" ] &&
            out="$cc"
        [ "$(echo $out | cut -f3)" = "$name" ] &&
            name=''
        echo -e "$out\t$name"    |
            sed -r 's/\s+$//'    |
            sed -r "s/\t/': ['/" |
            sed -r "s/\t/', '/g" |
            sed -r "s/^/'/"      |
            sed -r 's/$/'"'"',],/'
    done < input/cc.list  # cc.list from jVectorMap; format: lines start with ISO3166_alpha2_code else copied as is

Certain details updated by hand.
"""

CC_EUROPE = {
    '_0': ['Kosovo', 'Kosovo, Republic of'],
    '-99': ['N. Cyprus', 'North Cyprus'],
    'AD': ['AND', 'Andorra'],
    'AL': ['ALB', 'Albania'],
    'AT': ['AUT', 'Austria'],
    'AX': ['ALA', 'Åland Islands', 'Aland'],
    'BA': ['BIH', 'Bosnia and Herzegovina', 'Bosnia and Herz.'],
    'BE': ['BEL', 'Belgium'],
    'BG': ['BGR', 'Bulgaria'],
    'BY': ['BLR', 'Belarus'],
    'CH': ['CHE', 'Switzerland'],
    'CY': ['CYP', 'Cyprus'],
    'CZ': ['CZE', 'Czech Republic', 'Czech Rep.'],
    'DE': ['DEU', 'Germany'],
    'DK': ['DNK', 'Denmark'],
    'DZ': ['DZA', 'Algeria'],
    'EE': ['EST', 'Estonia'],
    'EG': ['EGY', 'Egypt'],
    'ES': ['ESP', 'Spain'],
    'FI': ['FIN', 'Finland'],
    'FO': ['FRO', 'Faroe Islands', 'Faeroe Is.'],
    'FR': ['FRA', 'France'],
    'GB': ['GBR', 'United Kingdom', 'Great Britain', 'England'],
    'GE': ['GEO', 'Georgia'],
    'GG': ['GGY', 'Guernsey'],
    'GR': ['GRC', 'Greece'],
    'HR': ['HRV', 'Croatia'],
    'HU': ['HUN', 'Hungary'],
    'IE': ['IRL', 'Ireland'],
    'IL': ['ISR', 'Israel'],
    'IM': ['IMN', 'Isle of Man'],
    'IQ': ['IRQ', 'Iraq'],
    'IS': ['ISL', 'Iceland'],
    'IT': ['ITA', 'Italy'],
    'JE': ['JEY', 'Jersey'],
    'JO': ['JOR', 'Jordan'],
    'LB': ['LBN', 'Lebanon'],
    'LI': ['LIE', 'Liechtenstein'],
    'LT': ['LTU', 'Lithuania'],
    'LU': ['LUX', 'Luxembourg'],
    'LV': ['LVA', 'Latvia'],
    'LY': ['LBY', 'Libya'],
    'MA': ['MAR', 'Morocco'],
    'MD': ['MDA', 'Moldova, Republic of', 'Moldova'],
    'ME': ['MNE', 'Montenegro'],
    'MK': ['MKD', 'Macedonia, Republic of', 'Macedonia'],
    'MT': ['MLT', 'Malta'],
    'NL': ['NLD', 'Netherlands'],
    'NO': ['NOR', 'Norway'],
    'PL': ['POL', 'Poland'],
    'PS': ['PSE', 'Palestine, State of', 'Palestine'],
    'PT': ['PRT', 'Portugal'],
    'RO': ['ROU', 'Romania'],
    'RS': ['SRB', 'Serbia'],
    'RU': ['RUS', 'Russian Federation', 'Russia'],
    'SA': ['SAU', 'Saudi Arabia'],
    'SE': ['SWE', 'Sweden'],
    'SI': ['SVN', 'Slovenia'],
    'SK': ['SVK', 'Slovakia'],
    'SM': ['SMR', 'San Marino'],
    'SY': ['SYR', 'Syrian Arab Republic', 'Syria'],
    'TN': ['TUN', 'Tunisia'],
    'TR': ['TUR', 'Turkey'],
    'UA': ['UKR', 'Ukraine'],
}


CC_WORLD = {
    # Does NOT include CC_EUROPE
    '_1': ['Somaliland'],
    'AE': ['ARE', 'United Arab Emirates'],
    'AF': ['AFG', 'Afghanistan'],
    'AM': ['ARM', 'Armenia'],
    'AO': ['AGO', 'Angola'],
    'AR': ['ARG', 'Argentina'],
    'AU': ['AUS', 'Australia'],
    'AZ': ['AZE', 'Azerbaijan'],
    'BD': ['BGD', 'Bangladesh'],
    'BF': ['BFA', 'Burkina Faso'],
    'BI': ['BDI', 'Burundi'],
    'BJ': ['BEN', 'Benin'],
    'BN': ['BRN', 'Brunei Darussalam', 'Brunei'],
    'BO': ['BOL', 'Bolivia, Plurinational State of', 'Bolivia'],
    'BR': ['BRA', 'Brazil'],
    'BS': ['BHS', 'Bahamas'],
    'BT': ['BTN', 'Bhutan'],
    'BW': ['BWA', 'Botswana'],
    'BZ': ['BLZ', 'Belize'],
    'CA': ['CAN', 'Canada'],
    'CD': ['COD', 'Congo, The Democratic Republic of the', 'Dem. Rep. Congo'],
    'CF': ['CAF', 'Central African Republic', 'Central African Rep.'],
    'CG': ['COG', 'Congo'],
    'CI': ['CIV', "Côte d'Ivoire"],
    'CL': ['CHL', 'Chile'],
    'CM': ['CMR', 'Cameroon'],
    'CN': ['CHN', 'China'],
    'CO': ['COL', 'Colombia'],
    'CR': ['CRI', 'Costa Rica'],
    'CU': ['CUB', 'Cuba'],
    'DJ': ['DJI', 'Djibouti'],
    'DO': ['DOM', 'Dominican Republic', 'Dominican Rep.'],
    'EC': ['ECU', 'Ecuador'],
    'EH': ['ESH', 'Western Sahara', 'W. Sahara'],
    'ER': ['ERI', 'Eritrea'],
    'ET': ['ETH', 'Ethiopia'],
    'FJ': ['FJI', 'Fiji'],
    'FK': ['FLK', 'Falkland Islands [Malvinas]', 'Falkland Is.'],
    'GA': ['GAB', 'Gabon'],
    'GH': ['GHA', 'Ghana'],
    'GL': ['GRL', 'Greenland'],
    'GM': ['GMB', 'Gambia'],
    'GN': ['GIN', 'Guinea'],
    'GQ': ['GNQ', 'Equatorial Guinea', 'Eq. Guinea'],
    'GT': ['GTM', 'Guatemala'],
    'GW': ['GNB', 'Guinea-Bissau'],
    'GY': ['GUY', 'Guyana'],
    'HN': ['HND', 'Honduras'],
    'HT': ['HTI', 'Haiti'],
    'ID': ['IDN', 'Indonesia'],
    'IN': ['IND', 'India'],
    'IR': ['IRN', 'Iran, Islamic Republic of', 'Iran'],
    'JM': ['JAM', 'Jamaica'],
    'JP': ['JPN', 'Japan'],
    'KE': ['KEN', 'Kenya'],
    'KG': ['KGZ', 'Kyrgyzstan'],
    'KH': ['KHM', 'Cambodia'],
    'KP': ['PRK', "Korea, Democratic People's Republic of", 'Dem. Rep. Korea', 'North Korea'],
    'KR': ['KOR', 'Korea, Republic of', 'Korea', 'South Korea'],
    'KW': ['KWT', 'Kuwait'],
    'KZ': ['KAZ', 'Kazakhstan'],
    'LA': ['LAO', "Lao People's Democratic Republic", 'Lao PDR'],
    'LK': ['LKA', 'Sri Lanka'],
    'LR': ['LBR', 'Liberia'],
    'LS': ['LSO', 'Lesotho'],
    'MG': ['MDG', 'Madagascar'],
    'ML': ['MLI', 'Mali'],
    'MM': ['MMR', 'Myanmar'],
    'MN': ['MNG', 'Mongolia'],
    'MR': ['MRT', 'Mauritania'],
    'MW': ['MWI', 'Malawi'],
    'MX': ['MEX', 'Mexico'],
    'MY': ['MYS', 'Malaysia'],
    'MZ': ['MOZ', 'Mozambique'],
    'NA': ['NAM', 'Namibia'],
    'NC': ['NCL', 'New Caledonia'],
    'NE': ['NER', 'Niger'],
    'NG': ['NGA', 'Nigeria'],
    'NI': ['NIC', 'Nicaragua'],
    'NP': ['NPL', 'Nepal'],
    'NZ': ['NZL', 'New Zealand'],
    'OM': ['OMN', 'Oman'],
    'PA': ['PAN', 'Panama'],
    'PE': ['PER', 'Peru'],
    'PG': ['PNG', 'Papua New Guinea'],
    'PH': ['PHL', 'Philippines'],
    'PK': ['PAK', 'Pakistan'],
    'PR': ['PRI', 'Puerto Rico'],
    'PY': ['PRY', 'Paraguay'],
    'QA': ['QAT', 'Qatar'],
    'RW': ['RWA', 'Rwanda'],
    'SB': ['SLB', 'Solomon Islands', 'Solomon Is.'],
    'SD': ['SDN', 'Sudan'],
    'SL': ['SLE', 'Sierra Leone'],
    'SN': ['SEN', 'Senegal'],
    'SO': ['SOM', 'Somalia'],
    'SR': ['SUR', 'Suriname'],
    'SS': ['SSD', 'South Sudan', 'S. Sudan'],
    'SV': ['SLV', 'El Salvador'],
    'SZ': ['SWZ', 'Swaziland'],
    'TD': ['TCD', 'Chad'],
    'TF': ['ATF', 'French Southern Territories', 'Fr. S. Antarctic Lands'],
    'TG': ['TGO', 'Togo'],
    'TH': ['THA', 'Thailand'],
    'TJ': ['TJK', 'Tajikistan'],
    'TL': ['TLS', 'Timor-Leste'],
    'TM': ['TKM', 'Turkmenistan'],
    'TT': ['TTO', 'Trinidad and Tobago'],
    'TW': ['TWN', 'Taiwan, Province of China', 'Taiwan'],
    'TZ': ['TZA', 'Tanzania, United Republic of', 'Tanzania'],
    'UG': ['UGA', 'Uganda'],
    'US': ['USA', 'United States', 'United States of America'],
    'UY': ['URY', 'Uruguay'],
    'UZ': ['UZB', 'Uzbekistan'],
    'VE': ['VEN', 'Venezuela, Bolivarian Republic of', 'Venezuela'],
    'VN': ['VNM', 'Viet Nam', 'Vietnam'],
    'VU': ['VUT', 'Vanuatu'],
    'YE': ['YEM', 'Yemen'],
    'ZA': ['ZAF', 'South Africa'],
    'ZM': ['ZMB', 'Zambia'],
    'ZW': ['ZWE', 'Zimbabwe'],
}


CC_USA = {
    'US-AK': ['AK', 'Alaska'],
    'US-AL': ['AL', 'Alabama'],
    'US-AR': ['AR', 'Arkansas'],
    'US-AZ': ['AZ', 'Arizona'],
    'US-CA': ['CA', 'California'],
    'US-CO': ['CO', 'Colorado'],
    'US-CT': ['CT', 'Connecticut'],
    'US-DC': ['DC', 'District of Columbia'],
    'US-DE': ['DE', 'Delaware'],
    'US-FL': ['FL', 'Florida'],
    'US-GA': ['GA', 'Georgia'],
    'US-HI': ['HI', 'Hawaii'],
    'US-IA': ['IA', 'Iowa'],
    'US-ID': ['ID', 'Idaho'],
    'US-IL': ['IL', 'Illinois'],
    'US-IN': ['IN', 'Indiana'],
    'US-KS': ['KS', 'Kansas'],
    'US-KY': ['KY', 'Kentucky'],
    'US-LA': ['LA', 'Louisiana'],
    'US-MA': ['MA', 'Massachusetts'],
    'US-MD': ['MD', 'Maryland'],
    'US-ME': ['ME', 'Maine'],
    'US-MI': ['MI', 'Michigan'],
    'US-MN': ['MN', 'Minnesota'],
    'US-MO': ['MO', 'Missouri'],
    'US-MS': ['MS', 'Mississippi'],
    'US-MT': ['MT', 'Montana'],
    'US-NC': ['NC', 'North Carolina', 'N. Carolina'],
    'US-ND': ['ND', 'North Dakota', 'N. Dakota'],
    'US-NE': ['NE', 'Nebraska'],
    'US-NH': ['NH', 'New Hampshire'],
    'US-NJ': ['NJ', 'New Jersey'],
    'US-NM': ['NM', 'New Mexico'],
    'US-NV': ['NV', 'Nevada'],
    'US-NY': ['NY', 'New York'],
    'US-OH': ['OH', 'Ohio'],
    'US-OK': ['OK', 'Oklahoma'],
    'US-OR': ['OR', 'Oregon'],
    'US-PA': ['PA', 'Pennsylvania'],
    'US-RI': ['RI', 'Rhode Island'],
    'US-SC': ['SC', 'South Carolina', 'S. Carolina'],
    'US-SD': ['SD', 'South Dakota', 'S. Dakota'],
    'US-TN': ['TN', 'Tennessee'],
    'US-TX': ['TX', 'Texas'],
    'US-UT': ['UT', 'Utah'],
    'US-VA': ['VA', 'Virginia'],
    'US-VT': ['VT', 'Vermont'],
    'US-WA': ['WA', 'Washington'],
    'US-WI': ['WI', 'Wisconsin'],
    'US-WV': ['WV', 'West Virginia'],
    'US-WY': ['WY', 'Wyoming'],
}

US_CITIES = {
    # From https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
    'US-AK': ['Anchorage'],
    'US-AL': ['Birmingham', 'Montgomery', 'Mobile', 'Huntsville'],
    'US-AR': ['Little Rock'],
    'US-AZ': ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Gilbert', 'Glendale', 'Scottsdale', 'Tempe', 'Peoria', 'Surprise'],
    'US-CA': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim', 'Santa Ana', 'Riverside', 'Stockton', 'Chula Vista', 'Irvine', 'Fremont', 'San Bernardino', 'Modesto', 'Oxnard', 'Fontana', 'Moreno Valley', 'Huntington Beach', 'Glendale', 'Santa Clarita', 'Garden Grove', 'Oceanside', 'Rancho Cucamonga', 'Santa Rosa', 'Ontario', 'Elk Grove', 'Corona', 'Lancaster', 'Palmdale', 'Salinas', 'Hayward', 'Pomona', 'Escondido', 'Sunnyvale', 'Torrance', 'Pasadena', 'Orange', 'Fullerton', 'Thousand Oaks', 'Visalia', 'Roseville', 'Concord', 'Simi Valley', 'Santa Clara', 'Victorville', 'Vallejo', 'Berkeley', 'El Monte', 'Downey', 'Costa Mesa', 'Carlsbad', 'Inglewood', 'Fairfield', 'Ventura', 'Temecula', 'Antioch', 'Richmond', 'West Covina', 'Murrieta', 'Norwalk', 'Daly City', 'Burbank', 'Santa Maria', 'El Cajon', 'San Mateo', 'Rialto', 'Clovis', 'East Los Angeles'],
    'US-CO': ['Denver', 'Colorado Springs', 'Aurora', 'Fort Collins', 'Lakewood', 'Thornton', 'Arvada', 'Westminster', 'Pueblo', 'Centennial', 'Boulder'],
    'US-CT': ['Bridgeport', 'New Haven', 'Stamford', 'Hartford', 'Waterbury'],
    'US-DC': ['Washington'],
    'US-FL': ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St. Petersburg', 'Hialeah', 'Tallahassee', 'Fort Lauderdale', 'Port St. Lucie', 'Cape Coral', 'Pembroke Pines', 'Hollywood', 'Miramar', 'Gainesville', 'Coral Springs', 'Miami Gardens', 'Clearwater', 'Pompano Beach', 'Palm Bay', 'West Palm Beach', 'Lakeland', 'Brandon'],
    'US-GA': ['Atlanta', 'Columbus', 'Augusta', 'Macon', 'Savannah', 'Athens', 'Sandy Springs'],
    'US-HI': ['Honolulu'],
    'US-IA': ['Des Moines', 'Cedar Rapids', 'Davenport'],
    'US-ID': ['Boise'],
    'US-IL': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville', 'Springfield', 'Peoria', 'Elgin'],
    'US-IN': ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend'],
    'US-KS': ['Wichita', 'Overland Park', 'Kansas City', 'Olathe', 'Topeka'],
    'US-KY': ['Louisville', 'Lexington'],
    'US-LA': ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Metairie'],
    'US-MA': ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge'],
    'US-MD': ['Baltimore'],
    'US-MI': ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Ann Arbor', 'Lansing'],
    'US-MN': ['Minneapolis', 'St. Paul', 'Rochester'],
    'US-MO': ['Kansas City', 'St. Louis', 'Springfield', 'Independence', 'Columbia'],
    'US-MS': ['Jackson'],
    'US-MT': ['Billings'],
    'US-NC': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston–Salem', 'Fayetteville', 'Cary', 'Wilmington', 'High Point'],
    'US-ND': ['Fargo'],
    'US-NE': ['Omaha', 'Lincoln'],
    'US-NH': ['Manchester'],
    'US-NJ': ['Newark', 'Jersey City', 'Paterson', 'Elizabeth'],
    'US-NM': ['Albuquerque', 'Las Cruces'],
    'US-NV': ['Las Vegas', 'Henderson', 'Reno', 'North Las Vegas', 'Paradise', 'Sunrise Manor', 'Spring Valley', 'Enterprise'],
    'US-NY': ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse'],
    'US-OH': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron', 'Dayton'],
    'US-OK': ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow'],
    'US-OR': ['Portland', 'Salem', 'Eugene', 'Gresham'],
    'US-PA': ['Philadelphia', 'Pittsburgh', 'Allentown'],
    'US-RI': ['Providence'],
    'US-SC': ['Columbia', 'Charleston', 'North Charleston'],
    'US-SD': ['Sioux Falls'],
    'US-TN': ['Memphis', 'Nashville', 'Knoxville', 'Chattanooga', 'Clarksville', 'Murfreesboro'],
    'US-TX': ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington', 'Corpus Christi', 'Plano', 'Laredo', 'Lubbock', 'Garland', 'Irving', 'Amarillo', 'Grand Prairie', 'Brownsville', 'McKinney', 'Pasadena', 'Frisco', 'Mesquite', 'McAllen', 'Killeen', 'Waco', 'Carrollton', 'Denton', 'Midland', 'Abilene', 'Beaumont', 'Odessa', 'Round Rock', 'Richardson', 'Wichita Falls', 'College Station', 'Pearland', 'Lewisville', 'Tyler'],
    'US-UT': ['Salt Lake City', 'West Valley City', 'Provo', 'West Jordan'],
    'US-VA': ['Virginia Beach', 'Norfolk', 'Chesapeake', 'Richmond', 'Newport News', 'Alexandria', 'Hampton', 'Arlington County'],
    'US-WA': ['Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Bellevue', 'Kent', 'Everett'],
    'US-WI': ['Milwaukee', 'Madison', 'Green Bay'],
}

# Extend USA with US_CITIES
for i in US_CITIES: CC_USA[i].extend(US_CITIES[i])

# Extend world with Europe and USA
CC_WORLD.update(CC_EUROPE)
CC_WORLD['US'].extend(i for v in CC_USA.values() for i in v[1:])


def _invert_mapping(dict):
    return {(v.lower() if len(v) > 3 else v): k for k in dict for v in dict[k]}


INV_CC_EUROPE = _invert_mapping(CC_EUROPE)
INV_CC_WORLD = _invert_mapping(CC_WORLD)
INV_CC_USA = _invert_mapping(CC_USA)

SET_CC_EUROPE = set(INV_CC_EUROPE.keys()) | set(INV_CC_EUROPE.values())
SET_CC_USA = set(INV_CC_USA.keys()) | set(INV_CC_USA.values())
