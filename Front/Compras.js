    const Vue = require('vue');
    
    const app = createApp({
      data() {
        return {
          idCompra: '',
          Fecha: '',
          IdMedicamento: '',
          Cantidad: '',
          Precio: '',
          total: '',
          IdTratamiento: '',
          IdPaciente: '',
          compras: [],
          eidCompra: '',
          eFecha: '',
          eCantidad: '',
          ePrecio: '',
          etotal: '',
          eidTratamiento: '',
          eIdPaciente: '',
          eIdMedicamento: '',
        };
      },
        methods: {
            showModal(id) {
                  this.$refs[id].show()
            },

            hideModal(id) {
                this.$refs[id].hide()
            },

            editCompra(idCompra, Fecha, Cantidad, Precio, total, IdTratamiento, IdPaciente, IdMedicamento) {

              axios.get('http://127.0.0.1:5000/compra/' + idCompra)
              .then(response => {
                this.eidCompra = idCompra;
                this.eFecha = Fecha;
                this.eCantidad = Cantidad;
                this.ePrecio = Precio;
                this.etotal = total;
                this.IdTratamiento = IdTratamiento;
                this.IdPaciente = IdPaciente;
                this.IdMedicamento = IdMedicamento;
                app.showModal('Editar')
              })
              .catch(err => {
                console.log(err)
              })
            },
      },

        mounted() {
            this.getTratamientos()
        }
    });
    app.mount('#vuejscrudapp')