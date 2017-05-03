(define (cube x)
  'YOUR-CODE-HERE
  (* x x x)
)

(define (over-or-under x y)
  'YOUR-CODE-HERE
  (cond ((> x y) 1)
		((= x y) 0)
		((< x y) -1))
)

(define (make-adder num)
  'YOUR-CODE-HERE
  (lambda (x) (+ x num))
)

(define structure
  'YOUR-CODE-HERE
  (cons (cons 1 '()) 
   		(cons 2
		 		(cons (cons 3 4)
					(cons 5 '()))))
)

(define (remove item lst)
  'YOUR-CODE-HERE
  (cond ((null? lst) '())
   		((equal? item (car lst)) (remove item (cdr lst)))
		 (else (cons (car lst) (remove item (cdr lst)))))  
)

