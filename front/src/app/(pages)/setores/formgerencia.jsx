import { useState } from "react";
import { Dialog, DialogContent, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

export default function FormGerencia({ open, handleClose }) {
  const [direcao, setDirecao] = useState("");
  const [gerencia, setGerencia] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Direção:", direcao, "Gerência:", gerencia);
    handleClose();
  };

  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent>
        <DialogTitle>Cadastro de Gerência</DialogTitle>
        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Campo Direção - Select */}
          <div>
            <Label htmlFor="direcao">Direção</Label>
            <Select onValueChange={setDirecao}>
              <SelectTrigger>
                <SelectValue placeholder="Selecione a direção" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="direcao1">Direção 1</SelectItem>
                <SelectItem value="direcao2">Direção 2</SelectItem>
                <SelectItem value="direcao3">Direção 3</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Campo Gerência - Input Texto */}
          <div>
            <Label htmlFor="gerencia">Gerência</Label>
            <Input
              id="gerencia"
              type="text"
              value={gerencia}
              onChange={(e) => setGerencia(e.target.value)}
              placeholder="Digite a gerência..."
              required
            />
          </div>

          {/* Botões */}
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={handleClose}>
              Cancelar
            </Button>
            <Button type="submit">Salvar</Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
