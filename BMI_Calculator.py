while True:
    try:
        userWeight = int(input('Enter your weight in pounds: '))
        userHeight = float(input('Enter your height (eg. 5foot 11inches = 5.11): '))
        userInches = (userHeight) * 12
        BMI = int(userWeight) * 703 / (userInches * userInches)
    except ValueError:
        print('Please provide valid input.')
        continue
    else: 
        if userWeight <= 0 or userHeight <= 0:
            print('Weight or Height cannot be zero or less.')
            continue
        else:
            BMI = round((userWeight) * 703 / (userInches * userInches),2)
            
            
            if BMI >= 40:
                classification = 'Morbidly Obese'
                healthRisk = 'Extremely High'
            elif BMI >= 35:
                classification = 'Severely Obese'
                healthRisk = 'Very High'
            elif BMI >= 30:
                classification = 'Obese'
                healthRisk = 'High'
            elif BMI >= 25:
                classification = 'Overweight'
                healthRisk = 'Increased'
            elif BMI >= 18.5:
                classification = 'Normal weight'
                healthRisk = 'Minimal'
            elif BMI < 18.5:
                classification = 'Under weight'
                healthRisk = 'Minimal'
            print(f'Your BMI is: {BMI}')
            print(f'Classification: {classification}')
            print(f'Health Risk: {healthRisk}')     
        break

