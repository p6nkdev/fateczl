.data
	msg1: .asciiz "\nDigite a primeira nota: "
	msg2: .asciiz "\nDigite a segunda nota: "
	msg3: .asciiz "\nDigite a terceira nota: "
	msg4: .asciiz "\nDigite a quarta nota: "
	msg5: .asciiz "\nMedia aritmetica: "
	msg6: .asciiz "\nAPROVADO"
	msg7: .asciiz "\nEXAME"
	msg8: .asciiz "\nRETIDO"

.text

main:
	# Lendo notas
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero

	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero

	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 5
	syscall
	add $t2, $v0, $zero

	li $v0, 4
	la $a0, msg4
	syscall
	li $v0, 5
	syscall
	add $t3, $v0, $zero

	# Calculando media inteira
	add $t4, $t0, $t1
	add $t4, $t4, $t2
	add $t4, $t4, $t3
	li $t5, 4
	div $t4, $t5
	mflo $t6

	# Imprimindo media
	li $v0, 4
	la $a0, msg5
	syscall
	li $v0, 1
	add $a0, $t6, $zero
	syscall

	# Verificando situacao
	li $t7, 6
	bge $t6, $t7, aprovado
	li $t7, 3
	bge $t6, $t7, exame
	j retido

aprovado:
	li $v0, 4
	la $a0, msg6
	syscall
	j fim

exame:
	li $v0, 4
	la $a0, msg7
	syscall
	j fim

retido:
	li $v0, 4
	la $a0, msg8
	syscall

fim:
	li $v0, 10
	syscall
