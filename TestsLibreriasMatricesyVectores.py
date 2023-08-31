import LibreriasMatricesyVectores as lm
import unittest

class TestCibreriaComplejos(unittest.TestCase):

    #Casos prueba de la suma
    def test_sumavectores(self):
        #Primer caso de prueba
        v1=lm.SumVec([3+4j,2-5j],[4+9j,3+8j])
        self.assertAlmostEqual(v1, [(7+13j), (5+3j)])
        #Segundo caso de prueba
        v2=lm.SumVec([2+2j,2-2j],[2+2j,2+2j])
        self.assertAlmostEqual(v2, [(4+4j), (4+0j)])
    def test_restavectores(self):
        #Primer caso de prueba
        v1=lm.ResVec([3+4j,2-5j],[4+9j,3+8j])
        self.assertAlmostEqual(v1, [(-1-5j), (-1-13j)])
        #Segundo caso de prueba
        v2=lm.ResVec([2+2j,2-2j],[2+2j,2+2j])
        self.assertAlmostEqual(v2, [(0-0j), (0-4j)])
    def test_multiplicacionescalarvector(self):
        #Primer caso de prueba
        v1=lm.mulVec([3+4j,2-5j],4)
        self.assertAlmostEqual(v1, [(12+16j), (8-20j)])
        #Segundo caso de prueba
        v2=lm.mulVec([2+2j,2-2j],2)
        self.assertAlmostEqual(v2, [(4+4j), (4-4j)])
    def test_sumamatrices(self):
        #Primer caso de prueba
        v1=lm.SumMat([[3+4j,2-5j],[4+3j,8-9j]],[[4+9j,3+8j],[4+3j,7+8j]])
        self.assertAlmostEqual(v1[0], [(7+13j), (5+3j)])
        self.assertAlmostEqual(v1[1], [(8+6j), (15-1j)])
        #Segundo caso de prueba
        v2=lm.SumMat([[2+2j,2+2j],[2+2j,2+2j]],[[2+2j,2+2j],[2+2j,2+2j]])
        self.assertAlmostEqual(v2[0], [(4+4j), (4+4j)])
        self.assertAlmostEqual(v2[1], [(4+4j), (4+4j)])
    def test_restamatrices(self):
        #Primer caso de prueba
        v1=lm.ResMat([[3+4j,2-5j],[4+3j,8-9j]],[[4+9j,3+8j],[4+3j,7+8j]])
        self.assertAlmostEqual(v1[0], [(-1-5j), (-1-13j)])
        self.assertAlmostEqual(v1[1], [0j, (1-17j)])
        #Segundo caso de prueba
        v2=lm.ResMat([[4+4j,4+4j],[4+4j,4+4j]],[[2+2j,2+2j],[2+2j,2+2j]])
        self.assertAlmostEqual(v2[0], [(2+2j), (2+2j)])
        self.assertAlmostEqual(v2[1], [(2+2j), (2+2j)])
    def test_multiplicacionescalarmatriz(self):
        #Primer caso de prueba
        v1=lm.mulMat([[3+4j,2-5j],[4+3j,8-9j]],4)
        self.assertAlmostEqual(v1[0], [(12+16j), (8-20j)])
        self.assertAlmostEqual(v1[1], [(16+12j), (32-36j)])
        #Segundo caso de prueba
        v2=lm.mulMat([[2+2j,2-2j],[2+2j,2-2j]],4)
        self.assertAlmostEqual(v2[0], [(8+8j), (8-8j)])
        self.assertAlmostEqual(v2[1], [(8+8j), (8-8j)])
    def test_transpuestavector(self):
        #Primer caso de prueba
        v1=lm.transpuestaVec([[3+4j, 2-5j]])
        self.assertAlmostEqual(v1[0], (3+4j))
        self.assertAlmostEqual(v1[1], (2-5j))
        #Segundo caso de prueba
        v2=lm.transpuestaVec([[5+4j, 2-3j]])
        self.assertAlmostEqual(v2[0], (5+4j))
        self.assertAlmostEqual(v2[1], (2-3j))
    def test_transpuestamatriz(self):
        #Primer caso de prueba
        v=lm.transpuestaMat([[3+4j,2-5j],[4+3j,8-9j]])
        self.assertAlmostEqual(v[0], [(3+4j), (4+3j)])
        self.assertAlmostEqual(v[1], [(2-5j), (8-9j)])
        #Segundo caso de prueba
        v=lm.transpuestaMat([[2+2j,4-4j],[5+5j,6-6j]])
        self.assertAlmostEqual(v[0], [(2+2j), (5+5j)])
        self.assertAlmostEqual(v[1], [(4-4j), (6-6j)])
    def test_conjugadovector(self):
        #Primer caso de prueba
        v1=lm.conVec([3+4j, 2-5j])
        self.assertAlmostEqual(v1, [(3-4j), (2+5j)])
        #Segundo caso de prueba
        v2=lm.conVec([-2-3j, 2-6j])
        self.assertAlmostEqual(v2, [(-2+3j), (2+6j)])
    def test_conjugadomatriz(self):
        #Primer caso de prueba
        v=lm.conMat([[3+4j,2-5j],[4+3j,8-9j]])
        self.assertAlmostEqual(v[0], [3-4j,2+5j])
        self.assertAlmostEqual(v[1], [4-3j,8+9j])
        #Segundo caso de prueba"""
        v=lm.conMat([[2+2j,2-2j],[2+3j,8-2j]])
        self.assertAlmostEqual(v[0], [2-2j,2+2j])
        self.assertAlmostEqual(v[1], [2-3j,8+2j])
if __name__ == '__main__':
    unittest.main()