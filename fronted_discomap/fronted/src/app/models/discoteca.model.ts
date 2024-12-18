export class Discoteca {
  id: number;
  nombre: string;
  direccion: string;
  horario_apertura: string;
  horario_cierre: string;
  aforo_maximo: number;
  stock_bebidas: string;
  calificacion: number;
  descripcion: string;
  created_at: string;
  imagen: string;
  telefono: string;
  redes_sociales: { [key: string]: string };
  precio_entrada: number | null;
  latitud: number | null;
  longitud: number | null;
  servicios: string;
  estado_abierta: boolean;
  promociones: string;
  user: any;

  constructor(init?: Partial<Discoteca>) {
    this.id = 0;
    this.nombre = '';
    this.direccion = '';
    this.horario_apertura = '';
    this.horario_cierre = '';
    this.aforo_maximo = 0;
    this.stock_bebidas = '';
    this.calificacion = 0;
    this.descripcion = '';
    this.created_at = '';
    this.imagen = 'assets/default-image.jpg';
    this.telefono = '';
    this.redes_sociales = {};
    this.precio_entrada = null;
    this.latitud = null;
    this.longitud = null;
    this.servicios = '';
    this.estado_abierta = false;
    this.promociones = '';
    this.user = {};
    Object.assign(this, init);
  }
}
