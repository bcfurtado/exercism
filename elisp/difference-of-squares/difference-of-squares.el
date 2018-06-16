;;; difference-of-squares.el --- Difference of Squares (exercism)

;;; Commentary:

;;; Code:

(defun square (number)
  (expt number 2))

(defun sum-of-squares (number)
  (apply '+ (mapcar 'square (number-sequence 1 number))))

(defun square-of-sums (number)
  (expt (apply '+ (number-sequence 1 number)) 2))

(defun difference (number)
  (- (square-of-sums number) (sum-of-squares number)))

(provide 'difference-of-squares)
;;; difference-of-squares.el ends here
