.data
	msg1: .asciiz "\nDigite um numero inteiro positivo: "
	msg2: .asciiz "\nValor negativo. Digite novamente."
	msg3: .asciiz "\nMaior valor: "
	msg4: .asciiz "\nMenor valor: "

.text

main:
	# Inicializando contador
	add $t0, $zero, $zero

ler_primeiro:
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	blt $t1, $zero, invalido_primeiro

	add $t2, $t1, $zero
	add $t3, $t1, $zero
	addi $t0, $t0, 1
	j ler_demais

invalido_primeiro:
	li $v0, 4
	la $a0, msg2
	syscall
	j ler_primeiro

ler_demais:
	li $t4, 10
	beq $t0, $t4, imprimir

	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	blt $t1, $zero, invalido_demais

	bgt $t1, $t2, novo_maior
	blt $t1, $t3, novo_menor
	addi $t0, $t0, 1
	j ler_demais

novo_maior:
	add $t2, $t1, $zero
	addi $t0, $t0, 1
	j ler_demais

novo_menor:
	add $t3, $t1, $zero
	addi $t0, $t0, 1
	j ler_demais

invalido_demais:
	li $v0, 4
	la $a0, msg2
	syscall
	j ler_demais

imprimir:
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 1
	add $a0, $t2, $zero
	syscall

	li $v0, 4
	la $a0, msg4
	syscall
	li $v0, 1
	add $a0, $t3, $zero
	syscall

	li $v0, 10
	syscall
