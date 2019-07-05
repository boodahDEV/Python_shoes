**Num_random**
    
    numpy.random.normal(loc=0.0, scale=1.0, size=None)
    Draw random samples from a normal (Gaussian) distribution.

    The probability density function of the normal distribution, first derived by De Moivre and 200 years later 
    by both Gauss and Laplace independently, is often called the bell curve because of its characteristic shape
    (see the example below).

    The normal distributions occurs often in nature. For example, it describes the commonly occurring distribution
    of samples influenced by a large number of tiny, random disturbances, each with its own unique distribution.

    Parameters:	
        loc : float or array_like of floats
              Mean (“centre”) of the distribution.

        scale : float or array_like of floats
                Standard deviation (spread or “width”) of the distribution.

        size : int or tuple of ints, optional
               Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. If size is
               None (default), a single value is returned if loc and scale are both scalars. Otherwise,
               np.broadcast(loc, scale). size samples are drawn.
    Returns:	
         out : ndarray or scalar
               Drawn samples from the parameterized normal distribution.
        
    The probability density for the Gaussian distribution is

            p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }} e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },

        where \mu is the mean and \sigma the standard deviation. The square of the standard deviation, \sigma^2, 
        is called the variance.
        
        The function has its peak at the mean, and its “spread” increases with the standard deviation 
        (the function reaches 0.607 times its maximum at x + \sigma and x - \sigma). This implies that 
        numpy.random.normal is more likely to return samples lying close to the mean, rather than those far away.

    
**Preguntas en clase** 

    Descripcion del problema:
     # Genere un programa que genere numeros aleatorios del 1 al 32000, Grafique el resultado
     # Genere un programa que genere numeros aleatorios Uniformes del 1 al 32000, Grafique el resultado
    
    ¿Que puede decir sobre ambas graficas?
      R:/ La diferencia entre cada grafica es que la grafica normal se representa mediante mecanismos de generación 
      de números seudoaleatorios, que, sin ser aleatorios (siguen una fórmula), lo aparentan.
      y en cuanto a la otra, Esta basada en la campana de Gauss como ya definido anteriormente.
    
    ¿Como es el comportamiento de los numeros aleatorios?
      R:/ Es imposible para una computadora generar números aleatorios (y por lo tanto generar cualquier evento aleatorio,
      puesto que todo dentro de una computadora se representa por medio de números). Lo que qquiero decir con esto es que,
      dado un conjunto de entradas siempre es posible determinar las salidas que producirá una computadora.
