(define (composed f g)
 (lambda (x) (f (g x)))
)

(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
  (cond ((or (= a 0) (= b 0)) (max a b))
   		((= (modulo (max a b) (min a b)) 0) (min a b))
   		(else (gcd(min a b) (modulo (max a b) (min a b)))))
)

(define (filter f lst)
  'YOUR-CODE-HERE
  (cond ((null? lst) nil)
   		((f (car lst)) (cons (car lst) (filter f (cdr lst))))
   		(else (filter f (cdr lst))))
)

(define (all-satisfies lst pred)
  'YOUR-CODE-HERE
  (cond ((null? lst) #t)
   		((pred (car lst)) (or (all-satisfies (cdr lst) pred) #t))
		(else #f))
  'standard version (= (length (filter pred lst) (length lst)))
)

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      'YOUR-CODE-HERE
	  (combiner (accumulate combiner
				 			start
							(- n 1)
							term)
	   			(term n))
      ))

