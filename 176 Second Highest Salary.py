#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:00:03 2018

@author: yiqian
"""

select max(e2.Salary) as SecondHighestSalary
from Employee e1,Employee e2
where e1.Salary>e2.Salary


"""
select second highest salary from table
"""
