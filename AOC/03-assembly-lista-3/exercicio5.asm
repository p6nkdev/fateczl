.data
	msg1: .asciiz "\nDigite o primeiro numero inteiro: "
	msg2: .asciiz "\nDigite o segundo numero inteiro: "
	msg3: .asciiz "\nA somatoria dos impares entre os valores e: "

.text

main:
	# Lendo primeiro numero
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Lendo segundo numero
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	# Definindo menor e maior
	bgt $t0, $t1, troca_limites
	add $t2, $t0, $zero
	add $t3, $t1, $zero
	j iniciar

troca_limites:
	add $t2, $t1, $zero
	add $t3, $t0, $zero

iniciar:
	addi $t2, $t2, 1
	add $t4, $zero, $zero

loop:
	bge $t2, $t3, imprimir
	andi $t5, $t2, 1
	beq $t5, $zero, proximo
	add $t4, $t4, $t2

proximo:
	addi $t2, $t2, 1
	j loop

imprimir:
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 1
	add $a0, $t4, $zero
	syscall

	li $v0, 10
	syscall
