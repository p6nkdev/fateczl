.data
msgNum1: .asciiz "Digite o primeiro valor: "
msgNum2: .asciiz "Digite o segundo valor: "
msgResto: .asciiz "Resto da divisao do maior pelo menor = "
msgErro: .asciiz "Nao e possivel dividir por zero.\n"

.text
.globl main
main:
    li $v0, 4
    la $a0, msgNum1
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgNum2
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    beq $t0, $zero, verificaSegundo
    beq $t1, $zero, erro
    j escolherMaior

verificaSegundo:
    beq $t1, $zero, erro

escolherMaior:
    bge $t0, $t1, primeiroMaior

    add $t2, $t1, $zero
    add $t3, $t0, $zero
    j calcular

primeiroMaior:
    add $t2, $t0, $zero
    add $t3, $t1, $zero

calcular:
    div $t2, $t3
    mflo $t4
    mul $t5, $t4, $t3
    sub $t6, $t2, $t5

    li $v0, 4
    la $a0, msgResto
    syscall

    li $v0, 1
    add $a0, $t6, $zero
    syscall

    li $v0, 10
    syscall

erro:
    li $v0, 4
    la $a0, msgErro
    syscall

    li $v0, 10
    syscall
