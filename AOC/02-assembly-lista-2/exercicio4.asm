.data
	msg1: .asciiz "\nDigite o salario atual: "
	msg2: .asciiz "\nNovo salario com aumento de 25%: "

.text

main:
	# Lendo salario atual
	li $v0, 4
	la $a0, msg1
	syscall

	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Calculando 25% do salario
	li $t1, 25
	mul $t2, $t0, $t1
	li $t3, 100
	div $t2, $t3
	mflo $t4

	# Somando aumento ao salario
	add $t5, $t0, $t4

	# Imprimindo resultado
	li $v0, 4
	la $a0, msg2
	syscall

	li $v0, 1
	add $a0, $t5, $zero
	syscall

	li $v0, 10
	syscall
