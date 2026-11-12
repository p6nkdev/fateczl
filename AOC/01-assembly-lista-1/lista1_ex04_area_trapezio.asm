.data
msgBaseMaior: .asciiz "Digite a base maior: "
msgBaseMenor: .asciiz "Digite a base menor: "
msgAltura: .asciiz "Digite a altura: "
msgArea: .asciiz "Area do trapezio = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgBaseMaior
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgBaseMenor
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    li $v0, 4
    la $a0, msgAltura
    syscall

    li $v0, 5
    syscall
    add $t2, $v0, $zero

    add $t3, $t0, $t1
    mul $t4, $t3, $t2
    li $t5, 2
    div $t4, $t5
    mflo $t4

    li $v0, 4
    la $a0, msgArea
    syscall

    li $v0, 1
    add $a0, $t4, $zero
    syscall

    li $v0, 10
    syscall
