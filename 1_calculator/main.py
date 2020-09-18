import Get_data
import Calculate

a = input('Please input the first parameter:')
b = input('Please input the operator:')
c = input('Please input the second parameter:')

data = Get_data.GetDate(a,b,c)
getAns = Calculate.Calculate(data)

print('The result is:',getAns.get_result())
