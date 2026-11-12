.data
	msg1: .asciiz "\nDigite o primeiro numero: "
	msg2: .asciiz "\nDigite o segundo numero: "
	msg3: .asciiz "\nOs numeros sao iguais"
	msg4: .asciiz "\nOs numeros sao diferentes"
	msg5: .asciiz "\nMaior valor: "
	msg6: .asciiz "\nMenor valor: "

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

	# Comparando valores
	beq $t0, $t1, iguais

	li $v0, 4
	la $a0, msg4
	syscall

	bgt $t0, $t1, primeiro_maior

	# Segundo maior
	li $v0, 4
	la $a0, msg5
	syscall

	li $v0, 1
	add $a0, $t1, $zero
	syscall

	li $v0, 4
	la $a0, msg6
	syscall

	li $v0, 1
	add $a0, $t0, $zero
	syscall
	j fim

primeiro_maior:
	li $v0, 4
	la $a0, msg5
	syscall

	li $v0, 1
	add $a0, $t0, $zero
	syscall

	li $v0, 4
	la $a0, msg6
	syscall

	li $v0, 1
	add $a0, $t1, $zero
	syscall
	j fim

iguais:
	li $v0, 4
	la $a0, msg3
	syscall

fim:
	li $v0, 10
	syscall
