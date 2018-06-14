;;; bob.el --- Bob exercise (exercism)

;;; Commentary:
;; We also can use string-join instead of mapconcat on emacs > 25.3 .

;;; Code:

(defun is-yelling (what)
  (and (equal (upcase what) what) (if (equal (downcase what) what) nil t)))

(defun is-a-question (what)
  (equal (substring (mapconcat 'identity (split-string what) " ") -1 nil) "?"))

(defun response-for (what)
  (cond ((eq (split-string what) nil) "Fine. Be that way!")
        ((and (is-yelling what) (is-a-question what) ) "Calm down, I know what I'm doing!")
        ((is-yelling what) "Whoa, chill out!")
        ((is-a-question what) "Sure.")
        (t "Whatever.")))


(provide 'bob)
;;; bob.el ends here
