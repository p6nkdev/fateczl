.data
	msg1: .asciiz "\nDigite o valor da compra entre 1000 e 9999: "
	msg2: .asciiz "\nValor invalido. Digite novamente."
	msg3: .asciiz "\nDigite o valor da parcela entre 100 e 500: "
	msg4: .asciiz "\nQuantidade de parcelas: "

.text

main:
le_compra:
	# Lendo valor da compra
	li $v0, 4
	la $a0, msg1
	syscall

	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Validando valor da compra
	li $t1, 1000
	blt $t0, $t1, compra_invalida
	li $t1, 9999
	bgt $t0, $t1, compra_invalida
	j le_parcela

compra_invalida:
	li $v0, 4
	la $a0, msg2
	syscall
	j le_compra

le_parcela:
	# Lendo valor da parcela
	li $v0, 4
	la $a0, msg3
	syscall

	li $v0, 5
	syscall
	add $t2, $v0, $zero

	# Validando valor da parcela
	li $t1, 100
	blt $t2, $t1, parcela_invalida
	li $t1, 500
	bgt $t2, $t1, parcela_invalida
	j calcular

parcela_invalida:
	li $v0, 4
	la $a0, msg2
	syscall
	j le_parcela

calcular:
	# Quantidade base de parcelas
	div $t0, $t2
	mflo $t3
	mfhi $t4

	# Se houver resto, soma mais uma parcela
	beq $t4, $zero, imprimir
	addi $t3, $t3, 1

imprimir:
	li $v0, 4
	la $a0, msg4
	syscall

	li $v0, 1
	add $a0, $t3, $zero
	syscall

	li $v0, 10
	syscall
