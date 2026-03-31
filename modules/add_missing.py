import pandas as pd
import numpy as np
 
def add_missing_and_clean(df):
    # Filling in missing data by replacing nulls with values advertised on the theme parks themselves website
    # from https://www.sixflags.com/kingsisland/attractions/the-great-pumpkin-coaster
    df.loc[(df['Name'] == 'Great Pumpkin Coaster') & (df['Park'] == "Kings Island"), 'Speed'] = '8 mph'

    # from https://www.sixflags.com/carowinds/attractions/carolina-goldrusher
    df.loc[(df['Name'] == 'Carolina Goldrusher') & (df['Park'] == "Carowinds"), 'Speed'] = '30 mph'
    df.loc[(df['Name'] == 'Carolina Goldrusher') & (df['Park'] == "Carowinds"), 'Height'] = '43 ft'

    # from https://www.sixflags.com/kingsisland/attractions/woodstock-express
    df.loc[(df['Name'] == 'Woodstock Express') & (df['Park'] == "Kings Island"), 'Speed'] = '35 mph'
    df.loc[(df['Name'] == 'Woodstock Express') & (df['Park'] == "Kings Island"), 'Height'] = '39 ft'

    # from https://www.sixflags.com/knotts/attractions/coast-rider
    df.loc[(df['Name'] == 'Coast Rider') & (df['Park'] == "Knott's Berry Farm"), 'Speed'] = '37 mph'


    # from https://www.sixflags.com/kingsdominion/attractions/grizzly
    df.loc[(df['Name'] == 'Grizzly') & (df['Park'] == 'Kings Dominion'), 'Speed'] = '51 mph'


    # from https://www.sixflags.com/dorneypark/attractions/woodstock-express
    df.loc[(df['Name'] == 'Woodstock Express') & (df['Park'] == 'Dorney Park'), 'Speed'] = '10 mph'

    # from https://www.sixflags.com/worldsoffun/attractions/cosmic-coaster
    df.loc[(df['Name'] == 'Cosmic Coaster') & (df['Park'] == 'Worlds of Fun'), 'Speed'] = '5 mph'
    df.loc[(df['Name'] == 'Cosmic Coaster') & (df['Park'] == 'Worlds of Fun'), 'Height'] = '15 ft'

    # from https://www.sixflags.com/valleyfair/attractions/cosmic-coaster
    df.loc[(df['Name'] == 'Cosmic Coaster') & (df['Park'] == 'Valleyfair'), 'Speed'] = '20 mph'
    df.loc[(df['Name'] == 'Cosmic Coaster') & (df['Park'] == 'Valleyfair'), 'Height'] = '14 ft'

    # from https://www.sixflags.com/magicmountain/attractions/canyon-blaster
    df.loc[(df['Name'] == 'Canyon Blaster') & (df['Park'] == 'Six Flags Magic Mountain'), 'Speed'] = '10 mph'

    # from https://finance.yahoo.com/news/six-flags-great-adventure-launch-070000570.html
    df.loc[(df['Name'] == 'Flash: Vertical Velocity') & (df['Park'] == 'Six Flags Great Adventure & Safari'), 'Height'] = '172 ft'

    # from https://coasterpedia.net/wiki/Runaway_Mine_Train_(Six_Flags_Great_Adventure)
    df.loc[(df['Name'] == 'Runaway Mine Train') & (df['Park'] == 'Six Flags Great Adventure & Safari'), 'Length'] = '2429 ft'


    # from https://www.sixflags.com/greatamerica/attractions/little-dipper
    df.loc[(df['Name'] == 'Little Dipper') & (df['Park'] == 'Six Flags Great America'), 'Speed'] = '20 mph'

    # from https://www.sixflags.com/overtexas/attractions/runaway-mine-train
    df.loc[(df['Name'] == 'Runaway Mine Train') & (df['Park'] == 'Six Flags Over Texas'), 'Speed'] = '35 mph'

    # from https://www.sixflags.com/overtexas/attractions/wile-e-coyotes-grand-canyon-blaster
    df.loc[(df['Name'] == "Wile E. Coyote's Grand Canyon Blaster") & (df['Park'] == 'Six Flags Over Texas'), 'Speed'] = '15 mph'
    df.loc[(df['Name'] == "Wile E. Coyote's Grand Canyon Blaster") & (df['Park'] == 'Six Flags Over Texas'), 'Speed'] = '15 mph'

    # from https://www.sixflags.com/overtexas/attractions/mini-mine-train
    df.loc[(df['Name'] == 'Mini Mine Train') & (df['Park'] == 'Six Flags Over Texas'), 'Speed'] = '20 mph'

    # from https://www.sixflags.com/fiestatexas/attractions/road-runner-express
    df.loc[(df['Name'] == 'Road Runner Express') & (df['Park'] == 'Six Flags Fiesta Texas'), 'Speed'] = '35 mph'

    # from https://www.sixflags.com/newengland/attractions/pandemonium
    df.loc[(df['Name'] == 'Pandemonium') & (df['Park'] == 'Six Flags Over Georgia'), 'Speed'] = '31 mph'
    df.loc[(df['Name'] == 'Pandemonium') & (df['Park'] == 'Six Flags Over Georgia'), 'Length'] = '1351 mph'

    # from https://www.sixflags.com/frontiercity/attractions/frankies-mine-train
    df.loc[(df['Name'] == "Frankie's Mine Train") & (df['Park'] == 'Six Flags Great Escape'), 'Speed'] = '16 mph'

    # from https://coasterpedia.net/wiki/Dragon_(Legoland_California)
    df.loc[(df['Name'] == 'Dragon') & (df['Park'] == 'Legoland California'), 'Speed'] = '28.5 mph'
    df.loc[(df['Name'] == 'Dragon') & (df['Park'] == 'Legoland California'), 'Height'] = '42.7 meters'

    # from https://www.altontowers.com/explore/theme-park/rides-attractions/runaway-mine-train/
    df.loc[(df['Name'] == 'Runaway Mine Train') & (df['Park'] == 'Alton Towers'), 'Height'] = '11 meters'

    # from https://www.altontowers.com/explore/theme-park/rides-attractions/the-smiler/
    df.loc[(df['Name'] == 'Smiler') & (df['Park'] == 'Alton Towers'), 'Height'] = '30 meters'

    # from https://www.altontowers.com/explore/theme-park/rides-attractions/spinball-whizzer/
    df.loc[(df['Name'] == 'Spinball Whizzer') & (df['Park'] == 'Alton Towers'), 'Speed'] = '60 kph'

    # from https://www.altontowers.com/explore/theme-park/rides-attractions/wicker-man/
    df.loc[(df['Name'] == 'Wicker Man') & (df['Park'] == 'Alton Towers'), 'Speed'] = '20 meters'

    # from https://coasterpedia.net/wiki/Vampire_(Chessington_World_of_Adventures)
    df.loc[(df['Name'] == 'Vampire') & (df['Park'] == 'Chessington World of Adventures'), 'Height'] = '21 meters'

    # from https://www.thorpepark.com/explore/theme-park/rides/saw-the-ride/
    df.loc[(df['Name'] == 'Saw - The Ride') & (df['Park'] == 'Thorpe Park'), 'Speed'] = '55 mph'

    # from https://www.universalorlando.com/web/en/us/things-to-do/rides-attractions/stardust-racers
    df.loc[(df['Name'] == 'Stardust Racers') & (df['Park'] == 'Epic Universe'), 'Length'] = '5000 ft'

    # from https://www.altontowers.com/explore/theme-park/rides-attractions/wicker-man/
    df.loc[(df['Name'] == 'Wicker Man') & (df['Park'] == 'Alton Towers'), 'Length'] = '20 m'

    # from https://disney.fandom.com/wiki/Matterhorn_Bobsleds
    df.loc[(df['Name'] == 'Matterhorn Bobsleds') & (df['Park'] == 'Disneyland'), 'Speed'] = '27 mph'

    # from https://disneyland.disney.go.com/attractions/disney-california-adventure/goofys-sky-school/
    df.loc[(df['Name'] == "Goofy's Sky School") & (df['Park'] == 'Disney California Adventure'), 'Length'] = '1200 ft'
    df.loc[(df['Name'] == "Goofy's Sky SChool") & (df['Park'] == 'Disney California Adventure'), 'Height'] = '55 ft'

    # from https://coasterpedia.net/wiki/Seven_Dwarfs_Mine_Train_(Magic_Kingdom)
    df.loc[(df['Name'] == 'Seven Dwarfs Mine Train') & (df['Park'] == 'Magic Kingdom'), 'Height'] = '41 ft'

    # from https://www.hersheypark.com/things-to-do/rides-and-attractions/laff-trakk
    df.loc[(df['Name'] == 'Laff Trakk') & (df['Park'] == 'Hersheypark'), 'Height'] = '51 ft'

    # from https://www.hersheypark.com/things-to-do/rides-and-attractions/sooperdooperlooper
    df.loc[(df['Name'] == 'Sooperdooperlooper') & (df['Park'] == 'Hersheypark'), 'Speed'] = '45 mph'
    df.loc[(df['Name'] == 'Sooperdooperlooper') & (df['Park'] == 'Hersheypark'), 'Height'] = '57 ft'

    # from https://buschgardens.com/williamsburg/roller-coasters/invadr/
    df.loc[(df['Name'] == 'InvadR') & (df['Park'] == 'Busch Gardens Williamsburg'), 'Height'] = '51 ft'

    # from https://coasterpedia.net/wiki/Verbolten
    df.loc[(df['Name'] == 'Verbolten') & (df['Park'] == 'Busch Gardens Williamsburg'), 'Height'] = '88 ft'

    # from https://coasterpedia.net/wiki/Big_Bad_Wolf:_The_Wolf%27s_Revenge
    df.loc[(df['Name'] == "Big Bad Wolf: The Wolf's Revenge") & (df['Park'] == 'Busch Gardens Williamsburg'), 'Height'] = '67 ft'

    # from https://coasterpedia.net/wiki/DarKoaster
    df.loc[(df['Name'] == "DarKoaster") & (df['Park'] == 'Busch Gardens Williamsburg'), 'Height'] = '37 ft'

    # from https://coasterpedia.net/wiki/Journey_to_Atlantis_(SeaWorld_Orlando)
    df.loc[(df['Name'] == 'Journey to Atlantis') & (df['Park'] == 'SeaWorld Orlando'), 'Height'] = '100 ft'

    # from https://timesofsandiego.com/arts/2023/06/01/need-speed-seaworlds-arctic-rescue-coaster-opens-friday/
    df.loc[(df['Name'] == 'Arctic Rescue') & (df['Park'] == 'SeaWorld San Diego'), 'Height'] = '30 ft'

    # from https://coasterpedia.net/wiki/Boulder_Dash_(Lake_Compounce)
    df.loc[(df['Name'] == 'Boulder Dash') & (df['Park'] == 'Lake Compounce'), 'Height'] = '110 ft'

    # from https://www.silverdollarcity.com/theme-park/attractions/rides/grand-exposition-coaster/
    df.loc[(df['Name'] == 'Grand Exposition Coaster') & (df['Park'] == 'Silver Dollar City'), 'Speed'] = '20 mph'

    # from https://www.startrek.com/news/operation-enterprise-officially-opens-at-movie-park-germany
    df.loc[(df['Name'] == 'Star Trek: Operation Enterprise') & (df['Park'] == 'MoviePark Germany'), 'Height'] = '40 m'

    # from https://coaster.cloud/en/attractions/b11a8454-gold-digger
    df.loc[(df['Name'] == 'Gold Digger') & (df['Park'] == 'MoviePark Germany'), 'Speed'] = '45 kph'

    # from https://coasterpedia.net/wiki/Big_Thunder_Mountain_Railroad_(Disneyland_Park)
    df.loc[(df['Name'] == 'Big Thunder Mountain Railroad') & (df['Park'] == 'Disneyland'), 'Height'] = '50 ft'

    # from https://coasterpedia.net/wiki/Incredicoaster
    df.loc[(df['Name'] == 'Incredicoaster') & (df['Park'] == 'Disney California Adventure'), 'Height'] = '120 ft'

    # from https://parkworld-online.com/space-fantasy-at-universal-studios-japan/
    df.loc[(df['Name'] == 'Space Fantasy - The Ride: Club Zedd Remix') & (df['Park'] == 'Universal Studios Japan'), 'Speed'] = '25 mph'

    # from https://www.visualterrain.net/portfolio/wild-eagle-dollywood/
    df.loc[(df['Name'] == 'Wild Eagle') & (df['Park'] == 'Dollywood'), 'Height'] = '210 ft'

    # from https://coasterpedia.net/wiki/Lightning_Rod
    df.loc[(df['Name'] == 'Lightning Rod') & (df['Park'] == 'Dollywood'), 'Height'] = '80 ft'

    #standardizing the length, removing units, and converting meters to feet
    def standardize_len(str_in):
        try:
            str_in = str_in.lower()
            str_in = str_in.strip()
            if 'ft' in str_in:
                str_in = str_in.replace('ft', '')
                output = float(str_in)
            elif 'meters' in str_in or 'm' in str_in:
                str_in = str_in.replace('meters', '')
                str_in = str_in.replace('m', '')
                output = float(str_in)
                output = 3.28084 * output
            else:
                output = np.nan
        except:
            output = np.nan
        return output
    #standardizing the speed, removing units, and converting kilometers per hour to miles per hour
    def standardize_speed(str_in):
        try:
            str_in = str_in.lower()
            str_in = str_in.strip()
            
            if 'mph' in str_in:
                str_in = str_in.replace('mph', '')
                output = float(str_in)
            elif 'kph' in str_in:
                str_in = str_in.replace('kph', '')
                output = float(str_in)
                output = 0.621371 * output
            else:
                output = np.nan
        except:
            output = np.nan
        return output

    #drop null values for any coasters that lack all the key values
    cleaned_df = df.dropna(subset = ['Height', 'Length', 'Speed'], how = 'all')
    cleaned_df['Park'] = cleaned_df['Park'].str.lower()
    cleaned_df['Name'] = cleaned_df['Name'].str.lower()
    cleaned_df['Chain'] = cleaned_df['Chain'].str.lower()
    cleaned_df.loc[:, 'Height'] = cleaned_df['Height'].apply(standardize_len)
    cleaned_df.loc[:, 'Length'] = cleaned_df['Length'].apply(standardize_len)
    cleaned_df.loc[:, 'Speed'] = cleaned_df['Speed'].apply(standardize_speed)

    return cleaned_df