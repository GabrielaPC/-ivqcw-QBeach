from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer, execute
from qiskit.visualization import plot_histogram

from numpy import pi

def Y(qc):
  qc.y(0)

def ZX(qc):
  qc.z(0)
  qc.x(0)

def mY(qc):
  qc.z(0)
  qc.x(0)
  qc.y(0)
  qc.z(0)
  qc.x(0)

def mZX(qc):
  qc.x(0)
  qc.z(0)


def roda_e_plota(cir, backend = "qasm_simulator"):
  be = BasicAer.get_backend(backend)
  job = execute(cir, be, shots=10)
  result = job.result()
  counts = result.get_counts(cir)
  print(counts)
  plot_histogram([counts])

def circuito_Y():
  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')
  circuit = QuantumCircuit(q, c)
  
  #estado de bell
  circuit.h(q)
  circuit.cz(q[0],q[1])
  
  #inserção de U 
  circuit.barrier(q[0], q[1])
  Y(circuit)
  circuit.barrier(q[0], q[1])
  
  
  # inversão sobre a média 
  circuit.h(q[0])
  circuit.h(q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.cz(q[0], q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.h(q[0])
  circuit.h(q[1])
  
  
  
  
  circuit.measure(q[0], c[0])
  circuit.measure(q[1], c[1])
  
  
  roda_e_plota(circuit)
  
def circuito_ZX():
  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')
  circuit = QuantumCircuit(q, c)
  
  #estado de bell
  circuit.h(q)
  circuit.cz(q[0],q[1])
  
  #inserção de U 
  circuit.barrier(q[0], q[1])
  ZX(circuit)
  circuit.barrier(q[0], q[1])
  
  
  # inversão sobre a média 
  circuit.h(q[0])
  circuit.h(q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.cz(q[0], q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.h(q[0])
  circuit.h(q[1])
  
  
  
  
  circuit.measure(q[0], c[0])
  circuit.measure(q[1], c[1])
  
  
  roda_e_plota(circuit)

def circuito_mY():
  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')
  circuit = QuantumCircuit(q, c)
  
  #estado de bell
  circuit.h(q)
  circuit.cz(q[0],q[1])
  
  #inserção de U 
  circuit.barrier(q[0], q[1])
  mY(circuit)
  circuit.barrier(q[0], q[1])
  
  
  # inversão sobre a média 
  circuit.h(q[0])
  circuit.h(q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.cz(q[0], q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.h(q[0])
  circuit.h(q[1])
  
  
  
  
  circuit.measure(q[0], c[0])
  circuit.measure(q[1], c[1])
  
  
  roda_e_plota(circuit)

def circuito_mZX():
  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')
  circuit = QuantumCircuit(q, c)
  
  #estado de bell
  circuit.h(q)
  circuit.cz(q[0],q[1])
  
  #inserção de U 
  circuit.barrier(q[0], q[1])
  mZX(circuit)
  circuit.barrier(q[0], q[1])
  
  
  # inversão sobre a média 
  circuit.h(q[0])
  circuit.h(q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.cz(q[0], q[1])
  circuit.x(q[0])
  circuit.x(q[1])
  circuit.h(q[0])
  circuit.h(q[1])
  
  
  
  
  circuit.measure(q[0], c[0])
  circuit.measure(q[1], c[1])
  
  
  roda_e_plota(circuit)
  
  

circuito_Y()
circuito_ZX()
circuito_mY()
circuito_mZX()