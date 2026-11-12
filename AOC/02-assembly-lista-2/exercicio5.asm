.data
	msg1: .asciiz "\nDigite o valor de A: "
	msg2: .asciiz "\nDigite o valor de B: "
	msg3: .asciiz "\nDigite o valor de C: "
	msg4: .asciiz "\nDUAS RAIZES REAIS"
	msg5: .asciiz "\nUMA RAIZ REAL"
	msg6: .asciiz "\nNAO EXISTEM RAIZES REAIS"

.text

main:
	# Lendo A
	li $v0, 4
	la $a0, msg1
	syscall

	li $v0, 5
	syscall
	add $t0, $v0, $zero

	# Lendo B
	li $v0, 4
	la $a0, msg2
	syscall

	li $v0, 5
	syscall
	add $t1, $v0, $zero

	# Lendo C
	li $v0, 4
	la $a0, msg3
	syscall

	li $v0, 5
	syscall
	add $t2, $v0, $zero

	# Calculando delta = B*B - 4*A*C
	mul $t3, $t1, $t1
	li $t4, 4
	mul $t5, $t0, $t2
	mul $t5, $t5, $t4
	sub $t6, $t3, $t5

	# Verificando delta
	bgt $t6, $zero, duas_raizes
	beq $t6, $zero, uma_raiz
	blt $t6, $zero, nenhuma_raiz

duas_raizes:
	li $v0, 4
	la $a0, msg4
	syscall
	j fim

uma_raiz:
	li $v0, 4
	la $a0, msg5
	syscall
	j fim

nenhuma_raiz:
	li $v0, 4
	la $a0, msg6
	syscall

fim:
	li $v0, 10
	syscall
