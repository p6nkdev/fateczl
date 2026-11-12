.data
	msg1: .asciiz "\nDigite o raio da circunferencia: "
	msg2: .asciiz "\nO comprimento da circunferencia e: "

.text

main:
	# Lendo raio
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Calculando comprimento = 2 * PI * raio, com PI = 3
	li $t1, 2
	li $t2, 3
	mul $t3, $t0, $t1
	mul $t3, $t3, $t2

	# Imprimindo resultado
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 1
	add $a0, $t3, $zero
	syscall

	li $v0, 10
	syscall
