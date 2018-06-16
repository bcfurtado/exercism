;;; hamming.el --- Hamming (exercism)

;;; Commentary:

;;; Code:

(defun is-equal (nucleotides)
  (if (string= (car nucleotides) (cdr nucleotides)) 0 1))

(defun hamming-distance(normal mutation)
  (if (eq (length normal) (length mutation))
      (apply '+
             (mapcar 'is-equal
                     (mapcar* 'cons
                              (split-string (key-description normal))
                              (split-string (key-description mutation)))))
    (error  "Something went wrong")))



(provide 'hamming)
;;; hamming.el ends here
