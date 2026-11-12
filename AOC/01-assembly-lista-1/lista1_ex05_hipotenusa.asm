.data
msgCateto1: .asciiz "Digite o primeiro cateto: "
msgCateto2: .asciiz "Digite o segundo cateto: "
msgHipotenusa: .asciiz "Hipotenusa = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgCateto1
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgCateto2
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    mul $t2, $t0, $t0
    mul $t3, $t1, $t1
    add $t4, $t2, $t3

    mtc1 $t4, $f0
    cvt.s.w $f0, $f0
    sqrt.s $f12, $f0

    li $v0, 4
    la $a0, msgHipotenusa
    syscall

    li $v0, 2
    syscall

    li $v0, 10
    syscall
