def check_eligibility(data):
    country_rules = {
        'australia': lambda d: d['education'] in ['bachelor', 'master', 'phd'] and d['experience'] >= 2,
        'switzerland': lambda d: d['education'] in ['master', 'phd'] and d['language'] == 'fluent',
        'japan': lambda d: d['education'] in ['bachelor', 'master'] and d['experience'] >= 1,
        'turkey': lambda d: d['education'] in ['high_school', 'bachelor'] and d['experience'] >= 1,
        'usa': lambda d: d['education'] in ['bachelor', 'master', 'phd'] and d['language'] != 'basic',
    }
    country = data['country']
    eligibility = country_rules[country](data)
    return "Eligible" if eligibility else "Not Eligible"
