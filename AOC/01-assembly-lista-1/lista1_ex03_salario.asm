.data
msgHorasNormais: .asciiz "Horas normais trabalhadas: "
msgHorasExtras: .asciiz "Horas extras trabalhadas: "
msgDesconto: .asciiz "Valor do desconto: "
msgBruto: .asciiz "Salario bruto = R$ "
msgLiquido: .asciiz "\nSalario liquido = R$ "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgHorasNormais
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgHorasExtras
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    li $v0, 4
    la $a0, msgDesconto
    syscall

    li $v0, 5
    syscall
    add $t2, $v0, $zero

    li $t3, 10
    li $t4, 15

    mul $t5, $t0, $t3
    mul $t6, $t1, $t4
    add $t7, $t5, $t6
    sub $t8, $t7, $t2

    li $v0, 4
    la $a0, msgBruto
    syscall

    li $v0, 1
    add $a0, $t7, $zero
    syscall

    li $v0, 4
    la $a0, msgLiquido
    syscall

    li $v0, 1
    add $a0, $t8, $zero
    syscall

    li $v0, 10
    syscall
