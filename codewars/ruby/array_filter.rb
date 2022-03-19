# Retrieve even numbers from array
# https://www.codewars.com/kata/514a6336889283a3d2000001

def get_even_numbers(arr)
  result = []
  arr.each do |num|
    result.push(num) if num % 2 == 0
  end
  result
end

# Result = [2,4,6]
puts(get_even_numbers([1,2,3,4,5,6]))
