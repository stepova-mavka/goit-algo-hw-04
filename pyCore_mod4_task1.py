def total_salary(file_path=str()):
    employee_count = int(0) # count employees for average salary
    salary_data = ()
    sal_sum = 0
    sal_avg = 0
    try:
        with open(file_path, 'r', encoding='UTF-8') as fh:
            while True:
                data = fh.readline()
                if data == '':
                    break
                sal_sum += int(data.split(',')[1]) # calculate salary sum
                employee_count += 1
        sal_avg = sal_sum/employee_count
        salary_data = (sal_sum, sal_avg) # write salary values into a tuple
    except FileNotFoundError:
        return print('File Not Found!!!!')
    else:
        return salary_data


salary_sum, salary_average = total_salary('D:/basic-projects/goit-algo-hw-04/monthly-salary.txt')

print(f"Загальна сума заробітної плати: {salary_sum}, Середня заробітна плата: {salary_average}")