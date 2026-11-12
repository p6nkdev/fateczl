.data
	msg1: .asciiz "\nDigite o primeiro valor: "
	msg2: .asciiz "\nDigite o segundo valor: "
	msg3: .asciiz "\nPrimeiro registrador apos a troca: "
	msg4: .asciiz "\nSegundo registrador apos a troca: "

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

	# Trocando valores
	add $t2, $t0, $zero
	add $t0, $t1, $zero
	add $t1, $t2, $zero

	# Imprimindo primeiro registrador
	li $v0, 4
	la $a0, msg3
	syscall

	li $v0, 1
	add $a0, $t0, $zero
	syscall

	# Imprimindo segundo registrador
	li $v0, 4
	la $a0, msg4
	syscall

	li $v0, 1
	add $a0, $t1, $zero
	syscall

	li $v0, 10
	syscall
