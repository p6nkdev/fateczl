.data
	msg1: .asciiz "\nDigite um numero entre 100 e 999: "
	msg2: .asciiz "\nValor invalido. Digite novamente."
	msg3: .asciiz "\nCENTENA = "
	msg4: .asciiz "\nDEZENA = "
	msg5: .asciiz "\nUNIDADE = "

.text

main:
leitura:
	# Lendo numero
	li $v0, 4
	la $a0, msg1
	syscall

	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Validando intervalo
	li $t1, 100
	blt $t0, $t1, invalido
	li $t1, 999
	bgt $t0, $t1, invalido
	j calcular

invalido:
	li $v0, 4
	la $a0, msg2
	syscall
	j leitura

calcular:
	# Centena
	li $t1, 100
	div $t0, $t1
	mflo $t2
	mfhi $t3

	# Dezena
	li $t1, 10
	div $t3, $t1
	mflo $t4
	mfhi $t5

	# Unidade
	add $t6, $t5, $zero

	# Imprimindo centena
	li $v0, 4
	la $a0, msg3
	syscall

	li $v0, 1
	add $a0, $t2, $zero
	syscall

	# Imprimindo dezena
	li $v0, 4
	la $a0, msg4
	syscall

	li $v0, 1
	add $a0, $t4, $zero
	syscall

	# Imprimindo unidade
	li $v0, 4
	la $a0, msg5
	syscall

	li $v0, 1
	add $a0, $t6, $zero
	syscall

	li $v0, 10
	syscall
