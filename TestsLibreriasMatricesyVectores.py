import LibreriasMatricesyVectores as lm
import unittest

class TestCibreriaComplejos(unittest.TestCase):

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
    def test_dagaVector(self):
        #Primer caso de prueba
        v=lm.dagaVector([1+4j, 2-5j])
        self.assertAlmostEqual(v, [(1-4j), (2+5j)])
        #Segundo caso de prueba
        v=lm.dagaVector([2+4j, 4-7j])
        self.assertAlmostEqual(v, [(2-4j), (4+7j)])
    def test_dagaMatriz(self):
        #Primer caso de prueba
        v=lm.dagaMatriz([[3+4j,2-5j],[4+3j,8-9j]])
        self.assertAlmostEqual(v[0], [3-4j, 4-3j])
        self.assertAlmostEqual(v[1], [2+5j, 8+9j])
        #Segundo caso de prueba
        v=lm.dagaMatriz([[5+7j,2-3j],[3+5j,2-3j]])
        self.assertAlmostEqual(v[0], [5-7j, 3-5j])
        self.assertAlmostEqual(v[1], [2+3j, 2+3j])
    def test_multiplicacionMatrices(self):
        #Primer caso de prueba
        v=lm.multiMatrices([[3+5j, 5-8j],[2+5j, 5+5j]], [[3+5j, 2+5j],[5-8j, 5+5j]])
        self.assertAlmostEqual(v, [[-55-50j, 46+10j],[46+10j, -21+70j]])
        #Segundo caso de prueba
        v=lm.multiMatrices([[3+4j,2-5j],[4+3j,8-9j]],[[5+7j,2-3j],[3+5j,2-3j]])
        self.assertAlmostEqual(v, [[18+36j, 7-17j], [68+56j, 6-48j]])
    def test_accionMatconVec(self):
        #Primer caso de prueba
        v=lm.accionMatVec([[3+4j,2-5j],[4+3j,8-9j]], [1+4j, 2-5j])
        self.assertAlmostEqual(v[0], [(-34-4j)])
        self.assertAlmostEqual(v[1], [(-37-39j)])
        #Segundo caso de prueba
        v=lm.accionMatVec([[5+7j,2-3j],[3+5j,2-3j]], [2+4j, 4-7j])
        self.assertAlmostEqual(v[0], [(-31+8j)])
        self.assertAlmostEqual(v[1], [(-27-4j)])
    def test_productoInterno(self):
        #Primer caso de prueba
        v=lm.productoInterno([1, 2+3j, 6j],[0, 1j, 2+4j])
        self.assertAlmostEqual(v, (27-10j))
        #Segundo caso de prueba
        v=lm.productoInterno([1+4j, 2-5j],[2+4j, 4-7j])
        self.assertAlmostEqual(v, (61+2j))
    def test_normaVec(self):
        #Primer caso de prueba
        v=lm.normaVec([1+4j, 2-5j])
        self.assertAlmostEqual(v, (0.9867451347791263+6.080597500329245j))
        #Segundo caso de prueba
        v=lm.normaVec([2+4j, 4-7j])
        self.assertAlmostEqual(v, (2.7575326737829853+7.252860569939335j))
    def test_distanciaVec(self):
        #Primer caso de prueba
        v=lm.distaciasVectores([1+4j, 2-5j],[2+4j, 4-7j])
        self.assertAlmostEqual(v, (2.1286448+1.8791298j))
        #Segundo caso de prueba
        v=lm.distaciasVectores([2+2j, 2-2j],[2+2j, 2-2j])
        self.assertAlmostEqual(v, 0)
    def test_matrizUnitaria(self):
        #Primer caso de prueba
        v=lm.matrizUnitaria([[23, -123j, 0],[123j, 23, 0],[0, 0, 1]])
        self.assertAlmostEqual(v, "Si es unitaria")
        #Segundo caso de prueba
        v=lm.matrizUnitaria([[23, -1j, 0],[123j, 23, 0],[0, 5, 1]])
        self.assertAlmostEqual(v, "No es unitaria")
    def test_matrizHermitiana(self):
        #Primer caso de prueba
        v=lm.matrizHermitiana([[5, 4+5j, 6-16j],[4-5j, 13, 7],[6+16j, 7, -2.1]])
        self.assertAlmostEqual(v, "Sí es hermitiana")
        #Segundo caso de prueba
        v=lm.matrizHermitiana([[23, -1j, 0],[123j, 23, 0],[0, 5, 1]])
        self.assertAlmostEqual(v, "No es hermitiana")
    def test_productoTensorV(self):
        #Primer caso de prueba
        v=lm.productoTensorV([2j, 1+6j],[-5j, 3+4j, -2.1])
        self.assertAlmostEqual(v, [(10-0j), (-8+6j), (-0-4.2j), (30-5j), (-21+22j), (-2.1-12.600000000000001j)])
        #Segundo caso de prueba
        v=lm.productoTensorV([2j, 6j], [2j, 3+2j, -2j])
        self.assertAlmostEqual(v, [(-4+0j), (-4+6j), (4-0j), (-12+0j), (-12+18j), (12-0j)])
if __name__ == '__main__':
    unittest.main()
