def car_profiler(make, model, **other_info):
    """Car profiler."""
    car_profile = {}
    car_profile['car_manufacturer'] = make
    car_profile['car_model'] = model
    for key, value in other_info.items():
        car_profile[key] = value
    return car_profile


car_profile = car_profiler(
    'subaru', 'outback', color='blue', tow_package='True',
    drive='4wd')
print(car_profile)
