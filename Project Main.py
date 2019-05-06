# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:34:05 2019

@author: Aquiles
"""
import pandas as pd
from matplotlib import pyplot
import itertools
import statsmodels.api as sm

#Interactive switch functions for messages
def sets_to_string(sets):
    switcher = {
        'r': "regions",
        'o': "airline codes",
        'c': "cities",
    }
    return switcher.get(sets, "?")

def time_to_string(time):
    switcher = {
        'd': "daily",
        'm': "monthly",
        'q': "quarterly",
        'y': "yearly",
    }
    return switcher.get(time, "?")

def analyze_to_string(analyze):
    switcher = {
        'o': "origin",
        'd': "destination",
        'v': "origin vs destination",
    }
    return switcher.get(analyze, "?")

#Choosing origin and destination - unique based on sets choice
def choose(sets, analyze):
    print("We will be choosing our origins and destinations now")
    #Default values
    tru = True;
    orig_city = None;
    dest_city = None;
    orig_region = None;
    dest_region = None;
    orig_code = None;
    dest_code = None;
    while tru == True:
#------------------------------------------Cities------------------------------
        if sets.lower() == 'c':
#---------------------------------Origin-------------------------------------
            if analyze.lower() == 'o':
                print("Please use the following origin city list as a reference: ")
                origin_city_list = df.origin_city.unique()
                print(origin_city_list)
                
                orig_city = input("Please enter your origin city from the list above(case + space sensitive): ")
                
                if orig_city in origin_city_list:
                    print("Origin City successfully applied ");
                    return orig_city, "default" if dest_city is None else dest_city;
                    tru = False;
                else:
                    print("Invalid origin city - please choose a valid origin city listed(case + space sensitive): ")
                    tru = True;
#---------------------------------Destination---------------------------------                    
            elif analyze.lower() == 'd':
                print("Please use the following destination city list as a reference: ")
                destination_city_list = df.destination_city.unique()
                print(destination_city_list);
                
                dest_city = input("Please enter your destination city from the list above(case + space sensitive): ")
                
                if dest_city in destination_city_list:
                    print("Destination City successfully applied");
                    return "default" if orig_city is None else orig_city, dest_city;
                    tru = False;
                else:
                    print("Invalid destination city - please choose a valid destination city listed(case + space sensitive): ")
                    tru = True;
#-------------------------------Origin vs Destination-------------------------
            elif analyze.lower() == 'v':
                print("Please use the following origin city list as a reference: ")
                origin_city_list = df.origin_city.unique()
                print(origin_city_list);
                    
                orig_city = input("Please enter your origin city from the list above(case + space sensitive): ")
               
                if orig_city in origin_city_list:
                    print("Origin City successfully applied");
                    print("Please use the following destination city list as a reference: ")
                    destination_city_list = df.destination_city.unique()
                    print(destination_city_list);
                        
                    dest_city = input("Please enter your destination city from the list above: ")
                    
                    
                    if dest_city in destination_city_list:
                        print("Destination City successfully applied");
                        return orig_city, dest_city;
                        tru = False;
                    else:
                        print("Invalid destination city - please choose a valid destination city from the list")
                        tru = True;

#-------------------------------Airline Codes---------------------------------
        elif sets.lower() == 'o':
#---------------------------------Origin-------------------------------------
            if analyze.lower() == 'o':
                print("Please use the following origin airport code list as a reference: ")
                origin_code_list = df.origin_airport_code.unique()
                print(origin_code_list);
                
                orig_code = input("Please enter your origin airport code from the list above: ")
                orig_code.strip();
                
                if orig_code.upper() in origin_code_list:
                    print("Origin Airport Code successfully applied ");
                    return orig_code.upper(), "default" if dest_code is None else dest_code;
                    tru = False;
                else:
                    print("Invalid origin airport code - please choose a valid origin airport code from the list ")
                    tru = True;
#---------------------------------Destination---------------------------------                    
            elif analyze.lower() == 'd':
                print("Please use the following destination airport code list as a reference: ")
                destination_code_list = df.dest_airport_code.unique()
                print(destination_code_list)
                
                dest_code = input("Please enter your destination airport code from the list above: ")
                dest_code.strip();
                
                if dest_code in destination_code_list:
                    print("Destination Airport Code successfully applied");
                    return "default" if orig_code is None else orig_code, dest_code.upper();
                    tru = False;
                else:
                    print("Invalid destination airport code - please choose a valid destination airport code listed: ")
                    tru = True;
#-------------------------------Origin vs Destination-------------------------
            elif analyze.lower() == 'v':
                print("Please use the following origin airport code list as a reference: ")
                origin_code_list = df.origin_airport_code.unique()
                print(origin_code_list)
                
                orig_code = input("Please enter your origin airport code from the list above: ")
                orig_code.strip();
                
                if orig_code.upper() in origin_code_list:
                    print("Origin Code successfully applied");
                    print("Please use the following destination airport code list as a reference: ")
                    destination_code_list = df.dest_airport_code.unique()
                    print(destination_code_list)
                    
                    dest_code = input("Please enter your destination airport code from the list above: ")
                    dest_code.strip();
                    
                    if dest_code.upper() in destination_code_list:
                        print("Destination City successfully applied");
                        return orig_code.upper(), dest_code.upper();
                        tru = False;
                    else:
                        print("Invalid destination airline code - please choose a valid destination airline code from the list")
                        tru = True;
                
#----------------------------------Regions-----------------------------------
        elif sets.lower() == 'r':
#---------------------------------Origin-------------------------------------
            if analyze.lower() == 'o':
                print("Please use the following origin region list as a reference: ")
                origin_region_list = df.origin_region.unique()
                print(origin_region_list)
                   
                orig_region = input("Please enter your origin region from the list above(case + space sensitive): ")
                
                if orig_region in origin_region_list:
                    print("Origin Region successfully applied ");
                    return orig_region, "default" if dest_region is None else dest_region;
                    tru = False;
                else:
                    print("Invalid origin city - please choose a valid origin city from the list(case + space sensitive) ")
                    tru = True;
#---------------------------------Destination---------------------------------                    
            elif analyze.lower() == 'd':
                print("Please use the following destination region list as a reference: ")
                destination_region_list = df.destination_region.unique()
                print(destination_region_list)
                
                dest_region = input("Please enter your destination region from the list above(case + space sensitive): ")
                
                if dest_region in destination_region_list:
                    print("Destination Region successfully applied");
                    return "default" if orig_region is None else orig_region, dest_region;
                    tru = False;
                else:
                    print("Invalid destination region - please choose a valid destination region listed(case + space sensitive) ")
                    tru = True;
#-------------------------------Origin vs Destination-------------------------
            elif analyze.lower() == 'v':
                print("Please use the following origin region list as a reference: ")
                origin_region_list = df.origin_region.unique()
                print(origin_region_list);
                   
                orig_region = input("Please enter your origin region from the list above(case + space sensitive): ")
                
                if orig_region in origin_region_list:
                    print("Origin Region successfully applied");
                    print("Please use the following destination region list as a reference: ")
                    destination_region_list = df.destination_region.unique()
                    print(destination_region_list)
                    
                    dest_region = input("Please enter your destination region from the list above(case + space sensitive): ")
                    
                    if dest_region in destination_region_list:
                        print("Destination Region successfully applied");
                        return orig_region, dest_region;
                        tru = False;
                    else:
                        print("Invalid destination region - please choose a valid destination region from the list")
                        tru = True;
                else:
                        print("Invalid origin region - please choose a valid origin region from the list")
                        tru = True;
           
    
    
#Acknowledgement of dataframes being used by user
def acknowledge(df_):
    true = True;
    tru = True;
    while tru == True:
        print(df_.head(10))
        print(df_.info())
        df_.plot(x = 'search_date', y = 'flight_demand', marker = 'o', figsize=(16,8), linestyle='None', markersize = 3.0)
        
        pyplot.show()
    
        ack = input("""This is the data you have requested. 
                        Is this okay? Y to acknowledge, N to choose another 
                        time table [X to exit code]: """)

        if ack.lower() == 'x':
            print("Request acknowledged - exiting program");
            true = False;
            tru = False;
            exit();
        elif ack.lower() == 'y':
            print("Request acknowledged - continuing program");
            true = False;
            tru = False;
        elif ack.lower() == 'n':
            print("""Request acknowledged - 
            restarting timetable program""");
            true = True;
            break
        else:
            print("""Input not acknowledged - please review 
            the data and choose an option:""")
            tru = True;
                
    return true;


#Functions called in order to create dataframes out of successive choices
def create_code_table(sets, analyze, orig_code="", dest_code=""):
    true = True
    while true == True:
        if sets.lower() == 'o' and analyze.lower() == 'o':
            df_ = df.loc[df['origin_airport_code'] == orig_code]
            true = acknowledge(df_)
        
        elif sets.lower() == 'o' and analyze.lower() == 'd':
            df_ = df.loc[df['dest_airport_code'] == dest_code]
            true = acknowledge(df_)
        
        elif sets.lower() == 'o' and analyze.lower() == 'v':
            df_ = df.loc[(df['dest_airport_code'] == dest_code) & 
                     (df['origin_airport_code'] == orig_code)]
            true = acknowledge(df_)
    df_ = df_.set_index(['search_date'])
    df_.index = pd.to_datetime(df_.index)         
    return df_

def create_city_table(sets, analyze, orig_city="", dest_city=""):
    true = True
    while true == True:
        if sets.lower() == 'c' and analyze.lower() == 'o':
            df_ = df.loc[df['origin_city'] == orig_city]
            true = acknowledge(df_)

        elif sets.lower() == 'c' and analyze.lower() == 'd':
            df_ = df.loc[df['destination_city'] == dest_city]
            true = acknowledge(df_)
        
        elif sets.lower() == 'c' and analyze.lower() == 'v':
            df_ = df.loc[(df['destination_city'] == dest_city) & 
                     (df['origin_city'] == orig_city)]
            true = acknowledge(df_)
    df_ = df_.set_index(['search_date'])
    df_.index = pd.to_datetime(df_.index)         
    return df_

def create_region_table(sets, analyze, orig_region="", dest_region=""):
    true = True
    while true == True:
        if sets.lower() == 'r' and analyze.lower() == 'o':
            df_ = df.loc[df['origin_region'] == orig_region]
            true = acknowledge(df_)
        
        elif sets.lower() == 'r' and analyze.lower() == 'd':
            df_ = df.loc[df['destination_region'] == dest_region]
            true = acknowledge(df_)
        
        elif sets.lower() == 'r' and analyze.lower() == 'v':
            df_ = df.loc[(df['destination_region'] == dest_region) & 
           (df['origin_region'] == orig_region)]
            true = acknowledge(df_)
    df_ = df_.set_index(['search_date'])
    df_.index = pd.to_datetime(df_.index)        
    return df_
        
    
def create_time_table(time):
    true = True
    tru = True
    while true == True:
        if time.lower() == 'q' or time.lower() == 'd' or time.lower() == 'y' or time.lower() == 'm':
            while tru == True:
                df__ = df_.resample(time.upper()).mean()
                print(df__.head(10))
                print(df__.info())
                df__.plot()
                pyplot.show()
                ack = input("""This is the data you have chosen to work with. 
                        Is this okay? Y to acknowledge, N to choose another 
                        time table [X to exit code]: """)
                if ack.lower() == 'x':
                    print("Request acknowledged - exiting program");
                    true = False;
                    tru = False;
                    exit;
                elif ack.lower() == 'y':
                    print("Request acknowledged - continuing program");
                    return df__;
                    true = False;
                    tru = False;
                elif ack.lower() == 'n':
                    print("""Request acknowledged - 
                            restarting timetable program""");
                    true = True;
                    tru = False;
                else:
                    print("""Input not acknowledged - please review 
                            the data and choose an option:""")
                    true = True;
                    tru = True; 
        elif time == 'x':
            print("Request acknowledged - exiting program");
            true = False;
            exit;
        return df__;
            
    
#Main body of program
print("""Welcome to our analytic program, where we will explore 
        multiple methods of data analytics in order to present
        our trend findings and extrapolate on future results""")

#Default parameters:
confirm = True;
dtypes={"search_date": 'str' , "origin_airport_code": 'str', 
        "origin_city": 'str', "origin_region": 'str', 
        "origin_country": 'str', "dest_airport_code": 'str', 
        "destination_city": 'str', "destination_region": 'str', 
        "destination_country": 'str', "flight_demand": 'int'};
sets = "";
time = "";
analyze = "";
df_ = pd.DataFrame(index=range(1,10))
df__ = df = pd.DataFrame(index=range(1,10))
results = []

#Creates original dataframe from csv file
print("Loading DataFrame, please wait...")
df = pd.read_csv("NY_FL_flight_demand.csv", header=[0], dtype=dtypes, 
                 engine='python')
df = df.set_index(pd.DatetimeIndex(df['search_date']))
print("Loading Complete")

#Begins loop after original dataframe build so that users do not have to keep rebuilding it
again = True
while again == True:
    #Asks the user for the kind of correlations they would like to make
    while confirm == True:
        sets = input("""Will we be looking for correlations between cities (C), regions 
                 (R), or airline codes (O)?[Press X to exit]: """ );
        sets.strip();
        if sets.lower() == 'c' or sets.lower() == 'r' or sets.lower() == 'o':
            
            #Interactive switch which assigns a string value to the sets choice made
            corString = sets_to_string(sets.lower())
        
            print("Acknowledged - we will be looking for correlations within " 
                  + corString)
            confirm = False; 
        elif sets.lower() == 'x':
            print("Request acknowledged - exiting program");
            confirm = False;
            exit;
        else:
            print("""Input not acknowledged - please review the question and choose 
                    an option:""")
            confirm = True;
    confirm = True;
    
    #Asks the user for origin, destination or a comparison of both 
    while confirm == True:
        analyze = input("""Will we be looking to analyze origins (O), 
                         destinations (D) or origins vs destination (V)?
                         [Press X to exit]: """ );
        analyze.strip();
        if sets.lower() == 'c':
            city = choose(sets, analyze)
            orig_city = city[0]
            dest_city = city[1]
            
            if analyze.lower() == 'o' or analyze.lower() == 'd' or analyze.lower() == 'v':
            
                #Interactive switch which assigns a string value to the sets choice made
                anaString = analyze_to_string(analyze.lower())
                print("Acknowledged - we will be looking to analyze " + anaString )
                
                df_ = create_city_table(sets, analyze, orig_city, dest_city)
                confirm = False; 
            elif analyze.lower() == 'x':
                print("Request acknowledged - exiting program");
                confirm = False;
                exit();
                
        elif sets.lower() == 'r':
            region = choose(sets, analyze)
            orig_region = region[0]
            dest_region = region[1]
            
            if analyze.lower() == 'o' or analyze.lower() == 'd' or analyze.lower() == 'v':
    
                anaString = analyze_to_string(analyze.lower())
                print("Acknowledged - we will be looking to analyze " + anaString )
                
                df_ = create_region_table(sets, analyze, orig_region, dest_region)
                confirm = False; 
            elif analyze.lower() == 'x':
                print("Request acknowledged - exiting program");
                confirm = False;
                exit();
                
        elif sets.lower() == 'o':
            code = choose(sets, analyze)
            orig_code = code[0]
            dest_code = code[1]
            
            if analyze.lower() == 'o' or analyze.lower() == 'd' or analyze.lower() == 'v':
    
                anaString = analyze_to_string(analyze.lower())
                print("Acknowledged - we will be looking to analyze " + anaString )
                
                df_ = create_code_table(sets, analyze, orig_code, dest_code)
                confirm = False; 
            elif analyze.lower() == 'x':
                print("Request acknowledged - exiting program");
                confirm = False;
                exit();
        else:
            print("""Input not acknowledged - please review the question and choose 
                    an option:""")
            confirm = True;
    confirm = True;
    
    #Asks the user how they would like to organize the time-based data
    while confirm == True:
        time = input("""How would you like to sample this data? Daily (D), 
                     Monthly (M), Quarterly (Q) or Yearly (Y)?[Press X to exit]: """)
        time.strip();
        if time.lower() == 'd' or time.lower() == 'm' or time.lower() == 'q' or time.lower() == 'y':
            
            #Interactive switch which assigns a string value to the time choice
            timeString = time_to_string(time.lower())
            
            print("Acknowledged - we will be organizing this data by " 
                   + timeString + " flight demand", end='\n\n')
            df__ = create_time_table(time)
            confirm = False; 
        elif time.lower() == 'x':
            print("Request acknowledged - exiting program", end='\n\n');
            confirm = False;
            exit();
        else:
            print("""Input not acknowledged - please review the question and choose 
                    an option:""", end='\n\n');
            confirm = True;
            
    #Creating range of p,d,q values to test
    p = d = q = range(0,2)
    com = list(itertools.product(p,d,q)) 
    com2 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p,d,q))]
    
    #iterate through all the combinations possible, checks AIC
    print("Calculating time-based series using ARIMA", end='\n\n')
    print("AIC Values are listed below:", end='\n\n')
    
    confirm = False;
    while(confirm == False):  
        
        count = 1;
        optrange = range(1,count)
        AICres = dict()
        for param in com:
            for param_seasonal in com2:
                try:
                    mod = sm.tsa.statespace.SARIMAX(df__,
                                                    order=param,
                                                    seasonal_order=param_seasonal,
                                                    enforce_stationarity = False,
                                                    enforce_invertibility=False)
                    results = mod.fit()
                    AICres.update({count: tuple([param,param_seasonal,results.aic])})
                    print('INDEX: {} - ARIMA{}x{}12 - AIC:{}'.format(count, param, param_seasonal, results.aic))
                    count += 1
                except:
                    continue
    
        index = int(input("Please choose which INDEX you would like to work with from the ones listed above: "))
        AICvalue = AICres[index]
        print("Attempting AIC value {}, please wait...".format(AICvalue[2]))
        try:
            mod = sm.tsa.statespace.SARIMAX(df__,
                                        order=AICvalue[0],
                                        seasonal_order=AICvalue[1],
                                        enforce_stationarity = False,
                                        enforce_invertibility=False)
            results = mod.fit()
            print(results.summary().tables[1])
            results.plot_diagnostics(figsize=(16, 8))
        except:
            pass
        
        print('Above is the model summary for param = {}, param_seasonal = {}, AIC = {}'.format(AICvalue[0], AICvalue[1], AICvalue[2]), end = '\n\n')
        ver = input('Would you like to work with this model? (Y,N); X to exit: ')
        
        if ver.lower() == 'y':
            print("Acknowledged - continuing program ", end = '\n\n')
            confirm = True
            pass
        elif ver.lower() == 'n':
            print("Acknowledged - rerunning AIC values: ", end = '\n')
            confirm = False
            pass
        elif ver.lower() == 'x':
            print("Exiting program safely! ", end = '\n')
            confirm = True
            exit();
        else:
            print("Invalid input - please read the instructions carefully: ", end = '\n\n')
            
    print("Validating our forecast...")
    fig, ax = pyplot.subplots(figsize=(19,6))
    pd.set_option('display.float_format', '{:.2f}'.format)
    #df___ is a dataframe using integer index in order to iloc date/time
    df___ = df__.reset_index()
    forecast = results.predict(start=df___.iloc[0,0], end=df___.iloc[-1,0])
    #df____ is the new predicted demand based on our ARIMA model
    df____ = pd.DataFrame(data=forecast,columns=['flight_demand'])
    df____.reset_index(drop=True)
    df____['search_date'] = [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in df___['search_date']]
    df___['search_date'] = [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in df___['search_date']]
    #plot predicted data
    pyplot.plot(df____['search_date'],df____['flight_demand'],label = 'Predicted')
    #plot actual data
    pyplot.plot(df___['search_date'],df___['flight_demand'],label = 'Actual')
    pyplot.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
    pyplot.title('Actual vs Predicted data')
    pyplot.legend()
    pyplot.show()
    print("You have reached the end of the main function!")
    repeat = input("Would you like to run this program again? Y to continue, any key to exit: ")
    if repeat.lower() == 'y':
        again = True;
    else:
        print("Exiting program - try again anytime!")
        again = False;
        exit();
        
    
