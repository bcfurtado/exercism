;;; gigasecond.el --- Gigasecond exercise (exercism)

;;; Commentary:
;; Calculate the date one gigasecond (10^9 seconds) from the
;; given date.
;;
;; NB: Pay attention to  Emacs' handling of time zones and dst
;; in the encode-time and decode-time functions.

;;; Code:

(defun from (seconds minutes hours day month year)
  (butlast (decode-time (time-add (encode-time seconds minutes hours day month year "UTC") (expt 10 9)) "UTC") 3))



(provide 'gigasecond)
;;; gigasecond.el ends here
