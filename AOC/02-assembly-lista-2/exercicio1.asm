.data
	msg1: .asciiz "\nDigite a altura do paralelepipedo: "
	msg2: .asciiz "\nDigite a largura do paralelepipedo: "
	msg3: .asciiz "\nDigite o comprimento do paralelepipedo: "
	msg4: .asciiz "\nO volume do paralelepipedo é: "
.text

main:
	# Pegando altura
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 5
	syscall
	add $t0, $v0, $zero
	
	# Pegando largura
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 5
	syscall
	add $t1, $v0, $zero
	
	# Pegando comprimento
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 5
	syscall
	add $t2, $v0, $zero
	
	# Calculando volume
	mul $v0, $v0, $t0
	mul $v0, $v0, $t1
	add $t3, $v0, $zero
	
	# Imprimindo resultado
	li $v0, 4
	la $a0, msg4
	syscall
	li $v0, 1
	add $a0, $t3, $zero
	syscall
	
	
	
