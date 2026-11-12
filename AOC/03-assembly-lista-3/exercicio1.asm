.data
	msg1: .asciiz "\nDigite o comprimento do paralelepipedo: "
	msg2: .asciiz "\nDigite a largura do paralelepipedo: "
	msg3: .asciiz "\nDigite a altura do paralelepipedo: "
	msg4: .asciiz "\nO volume do paralelepipedo e: "

.text

main:
	# Lendo comprimento
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Lendo largura
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	# Lendo altura
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 5
	syscall
	add $t2, $v0, $zero

	# Calculando volume
	mul $t3, $t0, $t1
	mul $t3, $t3, $t2

	# Imprimindo resultado
	li $v0, 4
	la $a0, msg4
	syscall
	li $v0, 1
	add $a0, $t3, $zero
	syscall

	li $v0, 10
	syscall
