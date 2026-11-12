.data
	msg1: .asciiz "\nDigite o primeiro valor inteiro: "
	msg2: .asciiz "\nDigite o segundo valor inteiro: "
	msg3: .asciiz "\nA diferenca do maior pelo menor e: "

.text

main:
	# Lendo primeiro valor
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Lendo segundo valor
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	# Calculando diferenca
	bgt $t0, $t1, primeiro_maior
	sub $t2, $t1, $t0
	j imprimir

primeiro_maior:
	sub $t2, $t0, $t1

imprimir:
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 1
	add $a0, $t2, $zero
	syscall

	li $v0, 10
	syscall
