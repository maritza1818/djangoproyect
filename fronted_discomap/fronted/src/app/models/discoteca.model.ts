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

  constructor(
    id: number,
    nombre: string,
    direccion: string,
    horario_apertura: string,
    horario_cierre: string,
    aforo_maximo: number,
    stock_bebidas: string,
    calificacion: number,
    descripcion: string,
    created_at: string,
    imagen: string,
    telefono: string,
    redes_sociales: { [key: string]: string },
    precio_entrada: number | null,
    latitud: number | null,
    longitud: number | null,
    servicios: string,
    estado_abierta: boolean,
    promociones: string,
    user: any
  ) {
    this.id = id;
    this.nombre = nombre;
    this.direccion = direccion;
    this.horario_apertura = horario_apertura;
    this.horario_cierre = horario_cierre;
    this.aforo_maximo = aforo_maximo;
    this.stock_bebidas = stock_bebidas;
    this.calificacion = calificacion;
    this.descripcion = descripcion;
    this.created_at = created_at;
    this.imagen = imagen || 'assets/default-image.jpg';
    this.telefono = telefono;
    this.redes_sociales = redes_sociales;
    this.precio_entrada = precio_entrada;
    this.latitud = latitud;
    this.longitud = longitud;
    this.servicios = servicios;
    this.estado_abierta = estado_abierta;
    this.promociones = promociones;
    this.user = user;
  }
}
