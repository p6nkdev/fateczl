.data
	msg1:      .asciiz "Digite n (>0): "
	resultado: .asciiz "Valor de H: "
.text

main:

# lendo n
ler_n:
	li $v0, 4
	la $a0, msg1
	syscall

	li $v0, 5
	syscall

	add $t0, $v0, $zero # t0 = n

	blez $t0, ler_n # se n <= 0, pede novamente

	# valores iniciais
	li $t1, 1 # i = 1
	li $t2, 0 # H = 0

# loop
loop:
	bgt $t1, $t0, fim # se i > n -> fim

	# verifica se i eh par ou impar
	andi $t3, $t1, 1 # pega o ultimo valor do binario (1 para impares, 0 para pares)

	beq $t3, $zero, par

	# se eh impar
	# termo = 1 * i
	add $t4, $t1, $zero
	add $t2, $t2, $t4

	j continua

# se eh par
# termo = 2 * i
par:
	mul $t4, $t1, 2
	add $t2, $t2, $t4

continua:
	addi $t1, $t1, 1
	j loop

# fim
fim:

	li $v0, 4
	la $a0, resultado
	syscall

	li $v0, 1
	add $a0, $t2, $zero
	syscall
