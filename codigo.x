#projeto de compilador para transformar ruby em script

puts "Insira dois números: "

puts "Valor de a"
a = gets.chomp.to_i

puts "Valor de b"
b = gets.chomp.to_i

puts "Escolha a operação:"
puts "1 . +"
puts "2 . -"
puts "3 . *"
puts "4 . /"

op = gets.chomp.to_i

if op == 1
  res = a + b
elsif op == 2
  res = a - b
elsif op == 3
  res = a * b
elsif op == 4
  res = a / b
else
  puts "Comando Inválido"
end

puts "Resultado: " + res