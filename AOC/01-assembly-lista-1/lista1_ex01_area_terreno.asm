.data
msgBase: .asciiz "Digite a base do terreno: "
msgAltura: .asciiz "Digite a altura do terreno: "
msgArea: .asciiz "Area do terreno = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgBase
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgAltura
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    mul $t2, $t0, $t1

    li $v0, 4
    la $a0, msgArea
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 10
    syscall
