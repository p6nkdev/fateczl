.data
msgA: .asciiz "Digite A: "
msgB: .asciiz "Digite B: "
msgC: .asciiz "Valor de C = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgA
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgB
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    beq $t0, $t1, soma

    mul $t2, $t0, $t1
    j mostrar

soma:
    add $t2, $t0, $t1

mostrar:
    li $v0, 4
    la $a0, msgC
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 10
    syscall
