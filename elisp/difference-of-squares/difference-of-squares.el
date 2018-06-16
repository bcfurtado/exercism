;;; difference-of-squares.el --- Difference of Squares (exercism)

;;; Commentary:

;;; Code:

(defun sum-of-squares (number)
  (if (> number 1) (+ (expt number 2) (sum-of-squares(1- number)) ) 1))

(defun sum-of-numbers-up-to (number)
  (if (> number 1) (+ number (sum-of-numbers-up-to(1- number)) ) 1))

(defun square-of-sums (number)
  (expt (sum-of-numbers-up-to number) 2))

(defun difference (number)
  (- (square-of-sums number) (sum-of-squares number)))

(provide 'difference-of-squares)
;;; difference-of-squares.el ends here
