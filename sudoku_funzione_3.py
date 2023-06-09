# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:14:37 2023

@author: alessandroamatori
"""

import random

def generate_incomplete_sudoku():
    # Inizializza una matrice vuota 9x9
    sudoku = [[0] * 9 for _ in range(9)]

    # Genera un Sudoku completo casuale
    for i in range(9):
        for j in range(9):
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(nums)
            sudoku[i][j] = nums.pop()

    # Rimuove alcune caselle casuali dal Sudoku
    for i in range(9):
        for j in range(9):
            if random.random() < 0.5:
                sudoku[i][j] = 0

    # Ritorna il Sudoku incompleto
    return sudoku

def play_sudoku():
    sudoku = generate_incomplete_sudoku()

    while True:
        print_sudoku(sudoku)
        row = int(input("Enter the row number (1-9): "))
        col = int(input("Enter the column number (1-9): "))
        num = int(input("Enter the number to insert (1-9): "))

        if not is_valid_move(sudoku, row - 1, col - 1, num):
            print("Invalid number! Please try again.")
            continue

        sudoku[row - 1][col - 1] = num

        play_again = input("Do you want to continue playing? (yes/no): ")
        if play_again.lower() == "no":
            break

def is_valid_move(sudoku, row, col, num):
    # Check if the number is already present in the same row or column
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # Check if the number is already present in the same 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True

def print_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if sudoku[i][j] == 0:
                print("  ", end="")
            else:
                print(str(sudoku[i][j]) + " ", end="")
        print()

play_sudoku()
