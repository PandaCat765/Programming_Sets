def savings(gross_pay, tax_rate, expenses):
	pay_after_tax = int(gross_pay * (1 - tax_rate))
	return pay_after_tax - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    used = num_jobs * job_consumption
    waste = total_material - used
    return str(waste) + material_units

def interest (principal, rate, periods):
    added_value = principal * (rate * periods)
    return int(principal + added_value)

